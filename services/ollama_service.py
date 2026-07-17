import ollama
from config.settings import CHAT_MODEL
from exceptions.exceptions import LLMResponseError
def ask_llm(prompt):
    try:
        response = ollama.chat(
            model=CHAT_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        return response["message"]["content"]
    except Exception as e:
        raise LLMResponseError() from e
