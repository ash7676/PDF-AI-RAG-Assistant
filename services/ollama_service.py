import ollama
from config.settings import CHAT_MODEL
def ask_llm(prompt):
    
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