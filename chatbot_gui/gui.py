import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

# Streamlit page settings
st.set_page_config(page_title="GBrit Chatbot", layout="centered")

# Custom CSS for chat bubbles
st.markdown("""
    <style>
    .user-msg {
        background: #DCF8C6;
        color: #202123;
        border-radius: 12px;
        padding: 10px 16px;
        margin: 6px 0;
        max-width: 75%;
        align-self: flex-end;
    }
    .bot-msg {
        background: #F1F0F0;
        color: #2d2d2d;
        border-radius: 12px;
        padding: 10px 16px;
        margin: 6px 0;
        max-width: 75%;
        align-self: flex-start;
    }
    .chat-thread {
        display: flex;
        flex-direction: column;
        gap: 2px;
        margin-bottom: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("GBrit Chatbot")

# Keep chat history in session
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat thread
st.markdown("<div class='chat-thread'>", unsafe_allow_html=True)
for chat in st.session_state.history:
    st.markdown(f"<div class='user-msg'><b>You:</b> {chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bot-msg'><b>Bot:</b> {chat['bot']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Function to send user input to backend
def send_message():
    user_input = st.session_state.user_message
    if user_input.strip():
        try:
            response = requests.post(f"{API_URL}/chat", json={"message": user_input})
            if response.status_code == 200:
                bot_reply = response.json().get("response", "")
                st.session_state.history.append({"user": user_input, "bot": bot_reply})
            else:
                st.error("API error.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
        # Clear input field after sending
        st.session_state.user_message = ""

# Text input with Enter key support, and Send button
st.text_input("You:", key="user_message", on_change=send_message)
st.button("Send", on_click=send_message)
