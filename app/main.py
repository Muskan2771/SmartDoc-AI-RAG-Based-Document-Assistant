import streamlit as st

from ui import setup_ui
from pdf_processor import load_and_split_pdf
from vector_store import create_vectorstore
from rag_pipeline import generate_answer

# ---------------------------
# UI SETUP
# ---------------------------

setup_ui()

# ---------------------------
# CHAT MEMORY
# ---------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# PDF UPLOAD
# ---------------------------

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

# ---------------------------
# PROCESS PDF
# ---------------------------

if uploaded_file and "retriever" not in st.session_state:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    documents = load_and_split_pdf("temp.pdf")

    retriever = create_vectorstore(documents)

    st.session_state.retriever = retriever

    st.success("PDF processed successfully!")

# ---------------------------
# SHOW CHAT HISTORY
# ---------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------------------
# USER INPUT
# ---------------------------

question = st.chat_input(
    "Ask your question..."
)

# ---------------------------
# GENERATE RESPONSE
# ---------------------------

if question:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    # Check retriever
    if "retriever" in st.session_state:

        answer = generate_answer(
            question,
            st.session_state.retriever
        )

    else:
        answer = "Please upload a PDF first."

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)