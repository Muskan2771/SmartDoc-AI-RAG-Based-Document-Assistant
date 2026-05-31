import os    #Access environment variables
from dotenv import load_dotenv  #load .env
from langchain_groq import ChatGroq   #Connects to Groq LLM


load_dotenv()   #Reads: GROQ_API_KEY=xxxx and makes it available to Python.

def load_llm():

    groq_api_key = os.getenv("GROQ_API_KEY")  #Gets API key.

    #Creates connection to the LLM.
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.1-8b-instant"
    )

    return llm