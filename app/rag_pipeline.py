from llm_handler import load_llm

llm = load_llm()

def generate_answer(question, retriever):

    relevant_docs = retriever.invoke(question)

    context = "\n".join([
        doc.page_content for doc in relevant_docs
    ])

    prompt = f"""
You are a helpful assistant.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content