from langchain_community.embeddings import HuggingFaceEmbeddings
# HuggingFaceEmbeddings, This converts text into numerical vectors (embeddings).

from langchain_community.vectorstores import FAISS
#FAISS stands for: Facebook AI Similarity Search
#Purpose: Store vectors, Search similar vectors quickly, Enable semantic search

def create_vectorstore(documents):

    #LangChain downloads and loads the model: sentence-transformers/all-MiniLM-L6-v2 ,This model converts text into vectors.
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        documents,
        embeddings
    )
    #This converts the vector database into a retriever object.
    #What is a Retriever?

    retriever=vectorstore.as_retriever()
    return retriever
