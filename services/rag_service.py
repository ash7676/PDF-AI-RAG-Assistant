from services.storage_service import load_documents
from services.search_service import search
from services.ollama_service import ask_llm
documents = load_documents()

def answer_question(question):
    # documents = load_documents()
    results = search(question,documents)
    context = "\n\n".join(
        result["chunk"] for result in results
    )
    final_prompt = f"""
    you are an HR assistant.
    Answer ONLY using the context below.
    If the answer is not present in the context, reply:
    "I could not find that information."
    Content:
    {context}
    Question:
    {question}
    """
    print("final prompt--",final_prompt)
    
    answer =  ask_llm(final_prompt)
    return answer