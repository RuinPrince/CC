import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.apps import apps
import chromadb
import requests

class Command(BaseCommand):
    help = 'Indexes ALL laws into ChromaDB for Semantic Search and RAG'

    def handle(self, *args, **kwargs):
        self.stdout.write("Initializing ChromaDB...")
        chroma_client = chromadb.PersistentClient(path=os.path.join(settings.BASE_DIR, 'chroma_db'))
        
        try:
            chroma_client.delete_collection("laws_collection")
        except Exception:
            pass
            
        collection = chroma_client.create_collection(name="laws_collection")

        OLLAMA_HOST = getattr(settings, 'OLLAMA_HOST', 'http://localhost:11434')
        OLLAMA_EMBED_MODEL = getattr(settings, 'OLLAMA_EMBED_MODEL', 'nomic-embed-text')
        OLLAMA_CHAT_MODEL = getattr(settings, 'OLLAMA_CHAT_MODEL', 'llama3')

        # Dynamically discover all law tables from the database
        try:
            LawTableList = apps.get_model('law', 'lawtablelist')
            law_tables = LawTableList.objects.all()
            models_to_index = []
            for lt in law_tables:
                try:
                    model = apps.get_model('law', lt.tname)
                    models_to_index.append((lt.tname, model))
                except LookupError:
                    self.stdout.write(self.style.WARNING(f"  Model '{lt.tname}' not found in law app, skipping."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Could not load LawTableList: {e}"))
            # Fallback: manually list known models
            from law.models import (Bns, ChildMarriage, ChildProtection, Electricity, IT,
                                     JuvenileJustice, MoneyLaundering, MotorVehicles,
                                     NationalHighways, PetroleumAndNaturalGas, WomenProtection,
                                     Wildlife, Realestate, Water, Muslimmarriage, Forest, Evs,
                                     Air, Companies, Hindumarriage, Specialmarriage,
                                     ConsumerProtection, Divorce)
            models_to_index = [
                ("Bns", Bns), ("ChildMarriage", ChildMarriage), ("ChildProtection", ChildProtection),
                ("Electricity", Electricity), ("IT", IT), ("JuvenileJustice", JuvenileJustice),
                ("MoneyLaundering", MoneyLaundering), ("MotorVehicles", MotorVehicles),
                ("NationalHighways", NationalHighways), ("PetroleumAndNaturalGas", PetroleumAndNaturalGas),
                ("WomenProtection", WomenProtection), ("Wildlife", Wildlife), ("Realestate", Realestate),
                ("Water", Water), ("Muslimmarriage", Muslimmarriage), ("Forest", Forest), ("Evs", Evs),
                ("Air", Air), ("Companies", Companies), ("Hindumarriage", Hindumarriage),
                ("Specialmarriage", Specialmarriage), ("ConsumerProtection", ConsumerProtection),
                ("Divorce", Divorce),
            ]

        # Also index rights models
        try:
            RightTableList = apps.get_model('right', 'righttablelist')
            right_tables = RightTableList.objects.all()
            for rt in right_tables:
                try:
                    model = apps.get_model('right', rt.tname)
                    models_to_index.append((rt.tname, model))
                except LookupError:
                    self.stdout.write(self.style.WARNING(f"  Model '{rt.tname}' not found in right app, skipping."))
        except Exception:
            pass

        self.stdout.write(f"Found {len(models_to_index)} models to index.")
        self.stdout.write("Starting indexing...")
        total_indexed = 0

        for act_name, model in models_to_index:
            self.stdout.write(f"Indexing {act_name}...")
            try:
                sections = model.objects.all()
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"  Could not query {act_name}: {e}"))
                continue
            
            count = 0
            for sec in sections:
                if hasattr(sec, 'description') and sec.description:
                    text = f"Act: {act_name}, Chapter: {getattr(sec, 'chapter', '')}, Title: {getattr(sec, 'title', '')}, Description: {sec.description}"
                    
                    try:
                        embedding = None
                        try:
                            r = requests.post(f"{OLLAMA_HOST}/api/embeddings", json={
                                "model": OLLAMA_EMBED_MODEL,
                                "prompt": text
                            }, timeout=10)
                            if r.status_code == 200:
                                embedding = r.json()["embedding"]
                        except Exception:
                            pass
                        
                        if not embedding:
                            r = requests.post(f"{OLLAMA_HOST}/api/embeddings", json={
                                "model": OLLAMA_CHAT_MODEL,
                                "prompt": text
                            }, timeout=15)
                            r.raise_for_status()
                            embedding = r.json()["embedding"]
                        
                        collection.add(
                            embeddings=[embedding],
                            documents=[text],
                            metadatas=[{"act": act_name, "section_id": str(sec.section), "title": getattr(sec, 'title', '')}],
                            ids=[f"{act_name}_{sec.section}"]
                        )
                        count += 1
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"  Error indexing {act_name} Section {sec.section}: {e}"))
            
            self.stdout.write(f"  Indexed {count} sections from {act_name}")
            total_indexed += count
        
        self.stdout.write(self.style.SUCCESS(f'Successfully indexed {total_indexed} law sections into ChromaDB!'))
