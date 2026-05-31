# 🤖 SmartDoc AI – RAG-Based Document Assistant

🔗 **Live Demo:** https://smartdoc-ai-rag-based-document-assistant-cq5stdgxfixhtk8dbkmzp.streamlit.app/

## 📌 Overview

SmartDoc AI is an intelligent Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and interact with them using natural language queries.

The system combines semantic document retrieval with Large Language Models (LLMs) to generate accurate, context-aware answers directly from uploaded documents. Instead of relying solely on model knowledge, responses are grounded in the document content, reducing hallucinations and improving reliability.

This project demonstrates practical implementation of Generative AI, Natural Language Processing (NLP), Vector Databases, and Large Language Models in a real-world customer support and document intelligence use case.

---

## ✨ Key Features

* 📄 Upload and analyze PDF documents
* 🔍 Semantic search using vector embeddings
* 🧠 Retrieval-Augmented Generation (RAG) pipeline
* 🤖 Context-aware AI responses powered by Groq LLaMA 3.1
* 💬 Interactive ChatGPT-style conversational interface
* ⚡ Fast inference using Groq API
* 📚 Multi-turn conversation support
* 🗂 Intelligent document chunking and retrieval
* 🔒 Environment variable-based API key management
* 🌐 Streamlit-based web application

---

## 🏗️ System Architecture

```text
User Uploads PDF
        │
        ▼
 PDF Text Extraction
        │
        ▼
 Document Chunking
        │
        ▼
 Embedding Generation
        │
        ▼
 FAISS Vector Store
        │
        ▼
 Semantic Retriever
        │
        ▼
 Relevant Context
        │
        ▼
 Groq LLaMA 3.1
        │
        ▼
 AI Generated Answer
```

---

## 📸 Application Screenshots

### Home Page

![Home](assets/home.png)

### Document Upload

![Upload](assets/upload.png)

### AI Chat Interface

![Chat](assets/chat.png)

---

## 🛠️ Technology Stack

| Category               | Technologies           |
| ---------------------- | ---------------------- |
| Programming Language   | Python                 |
| Frontend               | Streamlit              |
| LLM Framework          | LangChain              |
| Vector Database        | FAISS                  |
| Embedding Model        | HuggingFace Embeddings |
| LLM Provider           | Groq                   |
| Model                  | LLaMA 3.1              |
| Document Processing    | PyPDFLoader            |
| Environment Management | python-dotenv          |

---

## 📂 Project Structure

```bash
SmartDoc-AI/
│
├── app/
│   ├── llm_handler.py
│   ├── pdf_processor.py
│   ├── rag_pipeline.py
│   ├── vector_store.py
│   ├── ui.py
│   └── main.py
│
├── assets/
│   ├── architecture.png
│   ├── home.png
│   ├── upload.png
│   └── chat.png
│
├── data/
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/SmartDoc-AI.git
cd SmartDoc-AI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### 6. Run Application

```bash
streamlit run app/main.py
```

---

## 🔑 Environment Variables

| Variable     | Description  |
| ------------ | ------------ |
| GROQ_API_KEY | Groq API Key |

---

## 🧠 RAG Pipeline Workflow

### Step 1: Document Ingestion

* Upload PDF documents.
* Extract text using PyPDFLoader.

### Step 2: Text Chunking

* Split large documents into manageable chunks.
* Preserve contextual continuity using overlap.

### Step 3: Embedding Generation

* Convert text chunks into vector representations.
* Generate semantic embeddings using HuggingFace models.

### Step 4: Vector Storage

* Store embeddings in FAISS Vector Database.
* Enable efficient similarity search.

### Step 5: Retrieval

* Retrieve most relevant document chunks based on user query.

### Step 6: Response Generation

* Pass retrieved context to Groq LLaMA 3.1.
* Generate accurate, context-grounded responses.

---

## 🎯 Skills Demonstrated

### Generative AI

* Retrieval-Augmented Generation (RAG)
* Prompt Engineering
* Context Injection
* LLM Integration

### Natural Language Processing

* Semantic Search
* Text Embeddings
* Document Understanding
* Conversational AI

### Software Engineering

* Modular Architecture
* API Integration
* Environment Configuration
* Error Handling

### AI Infrastructure

* Vector Databases
* Similarity Search
* Document Retrieval Systems
* LLM Pipelines

---

## 📈 Future Enhancements

* Multi-document querying
* OCR support for scanned PDFs
* User authentication
* Conversation history database
* Docker containerization
* Cloud deployment (AWS/GCP/Azure)
* Advanced citation generation
* Source highlighting
* Multi-language support

---

## 📄 License

Licensed under the MIT License.

---

## 👩‍💻 Author

**Muskan Shaikh**

Aspiring AI/ML Engineer | Data Scientist | Generative AI Enthusiast

Passionate about building intelligent AI systems using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Natural Language Processing (NLP), Machine Learning, and Cloud Technologies.

### Connect With Me

* GitHub: https://github.com/Muskan2771/
* LinkedIn: https://www.linkedin.com/in/musu-shaikh/
* Email: [shaikhmuskan2771@gmail.com](mailto:shaikhmuskan2771@gmail.com)
