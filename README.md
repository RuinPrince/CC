# Civic Companion: Legal Intelligence Platform

Civic Companion is an advanced LegalTech platform built on Django 5.1.4. It provides structured access to Indian Laws with integrated AI assistance, semantic search, and document processing tools designed for professionals and citizens alike.

## Key Features

### 1. Security & Profiles
- **Secure Authentication:** JWT-based APIs.
- **Profiles:** Extended user data linked 1:1 with `django.contrib.auth.User`.
- **Throttling:** DRF rate-limiting (100/day for anon, 1000/day for authenticated users).
- **Audit Logging:** Admin actions are fully audited using `django-auditlog`.

### 2. Personalization
- **Bookmarks & Folders:** Save specific law sections into custom folders.
- **Personal Notes:** Add private annotations to any law.
- **Notifications:** Receive alerts for legal amendments.

### 3. AI & Advanced Search (RAG)
- **AI Legal Assistant:** Answers legal queries using OpenAI `gpt-3.5-turbo` grounded by your laws.
- **Semantic Search:** Vector search via `ChromaDB` and `text-embedding-ada-002` to bypass keyword limitations.
- **OCR Module:** Upload PDFs (via `pdfplumber`) or Images (via `pytesseract`) to extract text and analyze documents automatically.

### 4. Legal Utilities & Localization
- **Citation Generator:** Export laws in APA, MLA, Bluebook, and Indian formats.
- **PDF Reports:** Download laws and AI summaries natively via `reportlab`.
- **Amendment Tracking:** Monitor updates and relationships between sections.
- **Multilingual Support:** Core infrastructure laid out using `django-modeltranslation` for English, Tamil, Hindi, Telugu, Malayalam, and Kannada.

### 5. Analytics & Admin
- **Dashboard:** Sleek, modern admin UI powered by `django-jazzmin`.
- **API Documentation:** Interactive Swagger UI via `drf-yasg`.
- **Caching:** Performance optimization with Redis (`django-redis`).

## Setup Instructions

1. **Environment:** Create a virtual environment and install dependencies:
   `pip install -r requirements.txt` (including openai, chromadb, etc.)
2. **Database:** Migrate the database:
   `python manage.py makemigrations` and `python manage.py migrate`
3. **AI Indexing:** Index your existing SQLite laws into the vector database:
   `python manage.py index_laws`
4. **Redis Cache:** Ensure a Redis server is running on `localhost:6379`.
5. **Run Server:** 
   `python manage.py runserver`

## API Endpoints Overview
- **Auth:** `/api/users/login/`, `/api/users/register/`
- **Personalization:** `/api/bookmarks/`, `/api/notes/`
- **AI Tools:** `/api/ai/chat/`, `/api/ai/search/`, `/api/ai/ocr/`
- **Utilities:** `/api/utils/citation/`, `/api/utils/pdf/`
- **Docs:** `/swagger/`, `/redoc/`
