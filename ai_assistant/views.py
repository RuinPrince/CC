from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings
from django.db.models import Q
from django.apps import apps
import os
import requests

# Import each dependency independently so one missing lib doesn't break others
chroma_client = None
collection = None
try:
    import chromadb
    chroma_client = chromadb.PersistentClient(path=os.path.join(settings.BASE_DIR, 'chroma_db'))
    collection = chroma_client.get_or_create_collection(name="laws_collection")
except (ImportError, Exception):
    pass

pdfplumber = None
try:
    import pdfplumber as _pdfplumber
    pdfplumber = _pdfplumber
except ImportError:
    pass

pytesseract = None
Image = None
try:
    import pytesseract as _pytesseract
    from PIL import Image as _Image
    pytesseract = _pytesseract
    Image = _Image
except ImportError:
    pass

OLLAMA_HOST = getattr(settings, 'OLLAMA_HOST', 'http://localhost:11434')
OLLAMA_CHAT_MODEL = getattr(settings, 'OLLAMA_CHAT_MODEL', 'llama3')
OLLAMA_EMBED_MODEL = getattr(settings, 'OLLAMA_EMBED_MODEL', 'nomic-embed-text')

def get_ollama_embedding(text):
    """Get embedding from Ollama. Tries embed model first, falls back to chat model."""
    try:
        r = requests.post(f"{OLLAMA_HOST}/api/embeddings", json={
            "model": OLLAMA_EMBED_MODEL,
            "prompt": text
        }, timeout=10)
        if r.status_code == 200:
            return r.json()["embedding"]
    except Exception:
        pass
    
    try:
        r = requests.post(f"{OLLAMA_HOST}/api/embeddings", json={
            "model": OLLAMA_CHAT_MODEL,
            "prompt": text
        }, timeout=15)
        r.raise_for_status()
        return r.json()["embedding"]
    except Exception:
        raise ConnectionError("Could not get embeddings from Ollama. Is Ollama running?")

def query_ollama_chat(messages):
    """Query Ollama chat API."""
    r = requests.post(f"{OLLAMA_HOST}/api/chat", json={
        "model": OLLAMA_CHAT_MODEL,
        "messages": messages,
        "stream": False
    }, timeout=60)
    r.raise_for_status()
    return r.json()["message"]["content"]

def query_huggingface_chat(messages, hf_token=None):
    """Fallback: Query Hugging Face Inference API for chat completions."""
    if not hf_token:
        return None
    
    try:
        r = requests.post(
            'https://router.huggingface.co/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {hf_token}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'Qwen/Qwen2.5-72B-Instruct',
                'messages': messages,
                'max_tokens': 500
            },
            timeout=60
        )
        if r.status_code == 200:
            data = r.json()
            return data['choices'][0]['message']['content']
    except Exception:
        pass
    return None

class AIChatView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        query = request.data.get('query')
        hf_token = request.data.get('hf_token') or os.environ.get('HF_TOKEN') or os.environ.get('HUGGING_FACE_API_KEY') or ''
        if not query:
            return Response({"error": "Query is required"}, status=400)
        
        context = ""
        citations = []
        
        # 1. Try ChromaDB semantic search for context (RAG)
        if collection:
            try:
                query_embedding = get_ollama_embedding(query)
                results = collection.query(
                    query_embeddings=[query_embedding],
                    n_results=3
                )
                context_texts = results['documents'][0] if results['documents'] else []
                context = "\n\n".join(context_texts)
                citations = results['metadatas'][0] if results['metadatas'] else []
            except Exception:
                pass
        
        # 2. Build prompt
        prompt = f"You are a Senior Legal Assistant. Answer the user's question based ONLY on the following legal context. Explain in simple English.\n\nContext:\n{context}\n\nUser Question: {query}" if context else query
        
        messages = [
            {"role": "system", "content": "You are a helpful Legal Assistant for Indian Law."},
            {"role": "user", "content": prompt}
        ]

        # 3. Try local Ollama first
        try:
            answer = query_ollama_chat(messages)
            return Response({
                "answer": answer,
                "citations": citations,
                "source": "ollama"
            })
        except Exception:
            pass
        
        # 4. Fallback to Hugging Face Cloud API
        if hf_token:
            hf_answer = query_huggingface_chat(messages, hf_token)
            if hf_answer:
                return Response({
                    "answer": hf_answer,
                    "citations": citations,
                    "source": "huggingface"
                })
        
        return Response({
            "error": "AI is currently unavailable. Local Ollama is offline and no Hugging Face token was provided. Please set your HF token in the chat settings.",
            "citations": citations
        }, status=503)

class SemanticSearchView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        query = request.data.get('query')
        if not query:
            return Response({"error": "Query is required"}, status=400)
        
        # Try ChromaDB vector search first
        if collection:
            try:
                query_embedding = get_ollama_embedding(query)
                results = collection.query(
                    query_embeddings=[query_embedding],
                    n_results=10
                )

                formatted_results = []
                if results['documents']:
                    for i in range(len(results['documents'][0])):
                        formatted_results.append({
                            "text": results['documents'][0][i],
                            "metadata": results['metadatas'][0][i]
                        })
                return Response({"results": formatted_results})
            except Exception:
                pass
        
        # Fallback to SQL text search
        try:
            formatted_results = []
            law_tables = apps.get_model('law', 'lawtablelist').objects.all()
            for lt in law_tables:
                try:
                    model = apps.get_model('law', lt.tname)
                    matches = model.objects.filter(
                        Q(section__icontains=query) |
                        Q(title__icontains=query) |
                        Q(description__icontains=query)
                    )[:3]
                    for m in matches:
                        desc_text = m.description[:150] + "..." if len(m.description) > 150 else m.description
                        formatted_results.append({
                            "text": desc_text,
                            "metadata": {
                                "act": lt.tname,
                                "section_id": str(m.section),
                                "title": m.title or f"Section {m.section}"
                            }
                        })
                except Exception:
                    pass
            return Response({"results": formatted_results})
        except Exception as e:
            return Response({"error": f"Search failed: {str(e)}"}, status=500)

class OCRUploadView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_obj = request.FILES.get('document')
        if not file_obj:
            return Response({"error": "No document provided"}, status=400)
        
        extracted_text = ""
        file_name = file_obj.name.lower()
        
        try:
            if file_name.endswith('.pdf'):
                if pdfplumber is None:
                    return Response({"error": "PDF processing is not available (pdfplumber not installed)."}, status=500)
                with pdfplumber.open(file_obj) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:
                            extracted_text += text + "\n"
            elif file_name.endswith(('.png', '.jpg', '.jpeg')):
                if pytesseract is None or Image is None:
                    return Response({"error": "Image OCR is not available (pytesseract/Pillow not installed)."}, status=500)
                image = Image.open(file_obj)
                extracted_text = pytesseract.image_to_string(image)
            else:
                return Response({"error": "Unsupported file format. Please upload PDF or Images."}, status=400)

            return Response({"extracted_text": extracted_text.strip()})
        except Exception as e:
            return Response({"error": f"Failed to process document: {str(e)}"}, status=500)
