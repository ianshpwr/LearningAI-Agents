# streamlit_chatbot.py

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from pypdf import PdfReader

# Load environment variables
load_dotenv(override=True)

# Load Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Load LinkedIn PDF and extract text
reader = PdfReader("me/Linkedin.pdf")
linkedin = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin += text

# Load summary
with open("me/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

# Define system prompt
name = "Ansh"
system_prompt = f"""You are acting as {name}. You are answering questions on {name}'s website,
particularly questions related to {name}'s career, background, skills and experience.
Your responsibility is to represent {name} for interactions on the website as faithfully as possible.
You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions.
Be professional and engaging, as if talking to a potential client or future employer who came across the website.
If you don't know the answer, say so.

## Summary:
{summary}

## LinkedIn Profile:
{linkedin}

With this context, please chat with the user, always staying in character as {name}."""

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []  # list of (user, bot) tuples

st.title("🤖 Chat with Ansh")

# Display chat history
for user_msg, bot_msg in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)

# Chat input
prompt = st.chat_input("Ask Ansh anything about his career, background, or skills...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build the parts for Gemini
    parts = [{"text": system_prompt}]
    for u, b in st.session_state.history:
        parts.append({"text": u})
        parts.append({"text": b})
    parts.append({"text": prompt})

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_content(parts)
            bot_reply = response.text
            st.markdown(bot_reply)

    # Update session history
    st.session_state.history.append((prompt, bot_reply))
