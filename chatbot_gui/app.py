from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import ollama
import os

# FastAPI application instance
app = FastAPI(
    title="GBrit Chatbot API",
    description="Extended chatbot API with context-aware history for Streamlit GUI.",
    version="2.1.0"
)

# Expected request body
class ChatRequest(BaseModel):
    message: str

# In-memory chat history with initial system prompt
chat_history = [
    {"role": "system", "content": "You are GBrit Chatbot, a friendly assistant. Always reuse the user's name and details once given, and keep responses conversational."}
]

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "GBrit Chatbot API with context is live."}

# Main chat endpoint
@app.post("/chat")
async def chat(req: ChatRequest):
    user_message = req.message

    # Append user message to history
    chat_history.append({"role": "user", "content": user_message})

    try:
        # Send full history so model can respond with context
        response = ollama.chat(
            model="llama2",
            messages=chat_history
        )
        reply = response["message"]["content"]
    except Exception as e:
        reply = f"Error generating response: {str(e)}"

    # Append assistant reply
    chat_history.append({"role": "assistant", "content": reply})

    return {"response": reply}

# Endpoint to return entire conversation history
@app.get("/history")
def get_history():
    return {"history": chat_history}

# Serve favicon.ico (avoids 404 in browser tabs)
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(os.path.join(os.path.dirname(__file__), "favicon.ico"))
# Run the app with: uvicorn app:app --reload
