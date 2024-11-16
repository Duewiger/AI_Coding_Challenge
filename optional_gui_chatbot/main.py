from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from PyPDF2 import PdfReader
import openai
import os
from environs import Env

env = Env()
env.read_env()

OPENAI_API_KEY = env.str("OPENAI_API_KEY")

client = openai.OpenAI()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(request: ChatRequest):
    user_input = request.question
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    specific_context = None
    for file_name in content_collection:
        if file_name in user_input:
            specific_context = content_collection[file_name]
            break

    context = specific_context if specific_context else "\n\n".join(content_collection.values())
    messages.append({"role": "system", "content": context})
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=300,
        )
        reply = response.choices[0].message.content.strip()
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse("index.html")



# @app.post("/chat")
# async def chat(request: Request):
#     try:
#         body = await request.json()
#         question = body.get("question")
#         if not question:
#             raise HTTPException(status_code=400, detail="Question field is required")
#         return {"reply": f"Deine Frage war: {question}"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))