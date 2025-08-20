from fastapi import FastAPI
from pydantic import BaseModel
import ollama

# Initialize FastAPI app
app = FastAPI(
    title="GBrit Chatbot API",
    description="A simple RESTful AI chatbot service powered by FastAPI and Ollama (LLaMA2).",
    version="1.0.0"
)

# Define request body structure
class ChatRequest(BaseModel):
    message: str

# Root endpoint - health check
@app.get("/")
def read_root():
    return {"message": "GBrit Chatbot API is live..! Share your thoughts — let's find clarity together."}

# Chat endpoint
@app.post("/chat")
async def chat(req: ChatRequest):
    """
    Chat endpoint for GBrit Chatbot project.
    Expects a JSON body with a `message` string.
    Returns AI-generated response from LLaMA2 model.
    Example request:
    {
      "message": "Hello chatbot!"
    }
    """

    user_message = req.message

    # Call Ollama model (ensure Ollama service is running at localhost:11434)
    try:
        response = ollama.chat(
            model="llama2",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response["message"]["content"]

    except Exception as e:
        # Handle errors gracefully
        return {"error": f"Failed to generate response: {str(e)}"}

    return {"response": reply}
