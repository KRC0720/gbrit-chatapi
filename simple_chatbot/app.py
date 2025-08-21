from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import ollama
import os

# FastAPI app setup
app = FastAPI(
    title="GBrit Chatbot API",
    description="A simple REST API chatbot service powered by FastAPI and Ollama (LLaMA2).",
    version="1.0.0"
)

# Expected request body
class ChatRequest(BaseModel):
    message: str

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "GBrit Chatbot API is live..! Ready to chat."}

# Chat endpoint
@app.post("/chat")
async def chat(req: ChatRequest):
    """
    Send a message and receive a chatbot reply.
    Example:
    {
      "message": "Hello chatbot!"
    }
    """
    user_message = req.message

    try:
        # Forward message to local Ollama model (ensure it’s running)
        response = ollama.chat(
            model="llama2",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response["message"]["content"]
    except Exception as e:
        return {"error": f"Failed to generate response: {str(e)}"}

    return {"response": reply}

# Serve favicon (avoid 404 in browser tabs)
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(os.path.join(os.path.dirname(__file__), "favicon.ico"))
