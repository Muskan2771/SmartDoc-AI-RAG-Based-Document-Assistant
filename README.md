# 🤖 SmartDoc

An intelligent AI chatbot that uses **Retrieval Augmented Generation (RAG)** to answer questions from uploaded PDF documents. Built using LangChain, FAISS, Groq LLM, and Streamlit.

---

## 🚀 Features

- 📄 Upload and process PDF documents
- 🧠 AI understands document using embeddings
- 🔍 Semantic search using FAISS vector database
- 🤖 LLM-powered responses using Groq (LLaMA 3.1)
- 💬 ChatGPT-style conversational UI
- 🧾 Chat memory (multi-turn conversation)
- ⚡ Fast inference with Groq API
- 📚 Context-aware answers from documents

---

## 🧠 Architecture

PDF → Text Extraction → Chunking → Embeddings → FAISS Vector DB → Retrieval → LLM → Answer

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings
- Groq API (LLaMA 3.1)
- PyPDF

