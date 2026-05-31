from langchain_community.document_loaders import PyPDFLoader
#Used to read PDF files and convert them into LangChain Document objects.

from langchain_text_splitters import RecursiveCharacterTextSplitter
#RecursiveCharacterTextSplitter- Used to break large text into smaller chunks.

#Accepts a PDF file path.
def load_and_split_pdf(pdf_path):

    #Creates a PDF loader object.
    loader = PyPDFLoader(pdf_path)
    
    #Extracts text from all pages.
    docs = loader.load()
    
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    #chunk_size=1000, Each chunk can contain up to 1000 characters.
    #chunk_overlap=200, The last 200 characters of one chunk are repeated in the next chunk.
    
    documents = splitter.split_documents(docs)
    #Converts large pages into smaller chunks.

    return documents

"""
 PDF File
   │
   ▼
PyPDFLoader
   │
   ▼
Page Documents
   │
   ▼
RecursiveCharacterTextSplitter
(chunk_size=1000,
 chunk_overlap=200)
   │
   ▼
Small Text Chunks
   │
   ▼
Return Documents"""