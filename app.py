import streamlit as st
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

# ---------------------------
# LOAD ENV
# ---------------------------
load_dotenv()

# ---------------------------
# STREAMLIT UI
# ---------------------------
st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("🤖 AI Customer Support Chatbot (RAG)")

# ---------------------------
# CHAT MEMORY
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# PDF UPLOAD
# ---------------------------
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

# ---------------------------
# LOAD LLM
# ---------------------------
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# ---------------------------
# PROCESS PDF ONLY ONCE
# ---------------------------
if uploaded_file and "vectorstore" not in st.session_state:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    # Split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    documents = text_splitter.split_documents(docs)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector DB
    st.session_state.vectorstore = FAISS.from_documents(
        documents,
        embeddings
    )

    st.session_state.retriever = st.session_state.vectorstore.as_retriever()

    st.success("PDF processed successfully!")

# ---------------------------
# SHOW CHAT HISTORY (UI)
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------------------
# USER INPUT
# ---------------------------
question = st.chat_input("Ask your question...")

# ---------------------------
# RAG PIPELINE
# ---------------------------
if question:

    # store user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    # check if vector DB exists
    if "retriever" in st.session_state:

        # retrieve context
        relevant_docs = st.session_state.retriever.invoke(question)

        context = "\n".join([doc.page_content for doc in relevant_docs])

        # prompt
        prompt = f"""
You are a helpful customer support assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""

        # get response
        response = llm.invoke(prompt)
        answer = response.content

    else:
        answer = "Please upload a PDF first."

    # store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)