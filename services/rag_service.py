from services.search_service import search
from services.ollama_service import ask_llm
import logging

logger =  logging.getLogger(__name__)
def answer_question(question):
    results = search(question)
    context = "\n\n".join(
        results
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
    print()
    logger.info(f"final prompt: {final_prompt}")
    answer =  ask_llm(final_prompt)
    return answer