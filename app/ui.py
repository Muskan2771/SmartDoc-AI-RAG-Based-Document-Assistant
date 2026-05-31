import streamlit as st
#Imports the Streamlit library for building the web interface.

def setup_ui():


  st.set_page_config(
    page_title="RAG Chatbot", #Sets the browser tab title.
    layout="wide" #Makes the Streamlit application use the full browser width.
  )

  st.title("🤖 AI Customer Support Chatbot (RAG)")

