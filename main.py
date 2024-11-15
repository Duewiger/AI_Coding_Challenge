import os
import time
import openai
from environs import Env
from PyPDF2 import PdfReader

env = Env()
env.read_env()

OPENAI_API_KEY = env.str("OPENAI_API_KEY")

client = openai.OpenAI()

dataset_path = "./dataset_coding_challenge"
content_collection = {}

for file_name in os.listdir(dataset_path):
    file_path = os.path.join(dataset_path, file_name)
    
    if file_name.endswith(".pdf"):
        try:
            reader = PdfReader(file_path)
            pdf_text = ""
            for page in reader.pages:
                pdf_text += page.extract_text()
            content_collection[file_name] = pdf_text
            print(f"Inhalt von {file_name} erfolgreich extrahiert.\n")
        except Exception as e:
            print(f"Fehler beim Verarbeiten von {file_name}: {e}")


def chat_program():
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        user_input = input("Stell mir eine Frage: ")

        specific_context = None
        for file_name in content_collection:
            if file_name in user_input:
                specific_context = content_collection[file_name]
                break

        if specific_context:
            context = specific_context
        else:
            context = "\n\n".join(content_collection.values())
            
        messages.append({"role": "system", "content": context})
        messages.append({"role": "user", "content": user_input})

        try:
            # GPT-4o-mini API call
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=300,
            )
            reply = response.choices[0].message.content.strip()
            print(f"\n{reply}")
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"Fehler beim API-Aufruf: {e}")

        time.sleep(2)
        working_state = input("\nMöchtest du weitere Fragen stellen (j/n)?: ")
        
        if working_state.lower() == "j":
            continue
        else:
            print("Vielen Dank und auf Wiedersehen!")
            time.sleep(2)
            break

if __name__ == "__main__":
    chat_program()