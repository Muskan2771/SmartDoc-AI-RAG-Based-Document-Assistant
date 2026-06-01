import streamlit as st

from ui import setup_ui
from pdf_processor import load_and_split_pdf
from vector_store import create_vectorstore
from rag_pipeline import generate_answer

#ui setup
setup_ui() #Calls ui.py,  Responsible for:Page Title, Layout, Heading

#--------------------

#Session State-Think of it as temporary memory.
#Without it: User sends message --> Page reruns-->Message disappears
#With session state: User sends message-->Stored in memory-->Still visible

#Streamlit reruns the script whenever user interaction occurs. Session state is used to persist chat messages across reruns.

if "messages" not in st.session_state:
    st.session_state.messages = []

#--------------------

# PDF UPLOAD-Allows users to upload only PDF files.
uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

# ---------------------------

# PROCESS PDF

#Prevents reprocessing every time the page refreshes.
if uploaded_file and "retriever" not in st.session_state:
    
    #Creates a temporary file.
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    #load and split pdf
    documents = load_and_split_pdf("temp.pdf")
    
    #create retriever
    retriever = create_vectorstore(documents)
    
    #store retriever
    st.session_state.retriever = retriever

    st.success("PDF processed successfully!")

# ---------------------------
# SHOW/display CHAT HISTORY

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------------------
# USER INPUT
#Receives user query.
question = st.chat_input(
    "Ask your question..."
)

# ---------------------------
# GENERATE RESPONSE
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
        #generate ans
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
