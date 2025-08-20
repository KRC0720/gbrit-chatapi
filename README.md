
# GBrit Chatbot API

Hello, I’m **Ravichandran**  

This repository is my submission for the **GBrit Solutions hiring task**.  
The task was to build a **simple REST API chatbot** in Python that uses the **LLaMA model** (via Ollama) to return AI responses.  

---

## Requirements

Before starting, make sure you have:  

- **Python 3.10 or above**  
- **Pip** (Python’s package manager)  
- **Ollama** → install from [https://ollama.com/download](https://ollama.com/download)  

Test Ollama after installing by running:  

<pre>
ollama run llama3
</pre>

If the model responds, Ollama is installed correctly.  

- (Optional) **Postman** → [https://www.postman.com/downloads/](https://www.postman.com/downloads/) for testing APIs more easily.  

---

## Installation & Setup

### Clone the Repository

Cloning means making a local copy of this project from GitHub on your computer.  

Run:

<pre>
git clone https://github.com/KRC0720/gbrit-chatapi.git
</pre>

This will create a folder named **gbrit-chatapi** with all project files.  

Move into this folder:  

<pre>
cd gbrit-chatapi
</pre>

**Note:**  
Always run commands from *inside* this folder.  
Running them outside will cause errors like *“file not found”*.  

---

### Setup Virtual Environment

Create a virtual environment:  

<pre>
python -m venv venv
</pre>

Activate it:  

- On Linux/Mac:  
  <pre>source venv/bin/activate</pre>  

- On Windows:  
  <pre>venv\Scripts\activate</pre>  

---

### Install Dependencies

Install all required libraries:  

<pre>
pip install -r requirements.txt
</pre>

This will install:  
- `fastapi` – API framework  
- `uvicorn` – server runner  
- `pydantic` – validation  
- `requests` – HTTP requests  
- `ollama` – connector to LLaMA model  

---

## Running the Application

Start the FastAPI server:

<pre>
uvicorn app:app --reload
</pre>

If everything runs fine, you will see:

<pre>
Uvicorn running on http://127.0.0.1:8000
</pre>

This means the app is live at:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## API Endpoints

### 1. Health Check  
**GET /**

Sample response:

```
{ "message": "Chatbot API is running!" }
```

---

### 2. Chat Endpoint  
**POST /chat**

Request body (JSON):

```
{
  "message": "Hi, I am testing the chatbot!"
}
```

Example response:

```
{
  "response": "Hello Ravichandran! It's great to chat with you..."
}
```

**Tip:**  
If you see `422 Unprocessable Entity`, it usually means the request body is not valid JSON.  
Always send your input as:  
```
{ "message": "your text here" }
```

---

## Testing with Postman

This repo includes a ready Postman collection:  
`postman_collection.json`

Steps:  
1. Open Postman → Import → Select `postman_collection.json`  
2. You’ll find 3 pre‑saved requests:  
   - **Mindset (Q1)** – Sent to test how a fresher can prove like experienced.  
   - **Readiness (Q2)** – Explaining job‑readiness clearly.  
   - **AI Trends (Q3)** – Quick summary of 3 AI updates.  

Click **Send** and you’ll see chatbot responses instantly.  

---

## Notes on Common Issues

- **Wrong directory context:**  
  If you are not inside the `gbrit-chatapi` folder, commands like `uvicorn app:app --reload` will fail.  
  → Fix: Always run commands *inside* the project folder.  

- **Invalid JSON input to /chat endpoint:**  
  If you try to send plain text, it fails.  
  → Fix: Always wrap message in a JSON field: `{ "message": "hello" }`.  

- **Git push errors when uploading to GitHub:**  
  Sometimes errors like `src refspec main does not match any` occur if commits weren’t made before pushing.  
  → Fix: Run  
  <pre>
  git commit -m "Initial commit"
  git push -u origin main
  </pre>  

These notes are added so users can avoid wasting time with the same issues.  

---

## Project Structure

```
gbrit-chatapi/
├── app.py                  # FastAPI application
├── requirements.txt        # Python dependencies
├── postman_collection.json # Saved Postman requests
└── README.md               # Documentation
```

---

## Future Enhancements

- Save conversation history in a database  
- Add user authentication  
- Build a simple web UI for interactive chatting  

---

## Author

I am **Ravichandran**, an aspiring Data Science / AI professional.  
This project was developed as part of the hiring assignment at **GBrit Solutions**.  

I structured this README in a way that is **clear, beginner‑friendly, and notes potential pitfalls**,  
so that anyone reviewing this project can run it without issues.  

Thanks for checking out my work 🙏
```


