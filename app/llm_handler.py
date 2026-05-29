import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

# Load .env file
load_dotenv()

def load_llm():

    groq_api_key = os.getenv("GROQ_API_KEY")

    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.1-8b-instant"
    )

    return llm