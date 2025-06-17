from dotenv import load_dotenv
import google.generativeai as genai
from groq import Groq
from pypdf import PdfReader
import gradio as gr


load_dotenv(override=True)
model = genai.GenerativeModel('gemini-1.5-flash')

reader = PdfReader("me/Linkedin.pdf")
linkedin = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin += text

with open("me/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

name = "Ansh"

system_prompt = f"You are acting as {name}. You are answering questions on {name}'s website, \
particularly questions related to {name}'s career, background, skills and experience. \
Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer, say so."

system_prompt += f"\n\n## Summary:\n{summary}\n\n## LinkedIn Profile:\n{linkedin}\n\n"
system_prompt += f"With this context, please chat with the user, always staying in character as {name}."


def chatbot(message, history):
    parts = [{"text": system_prompt}]
    for user, bot in history:
        parts.append({"text": user})
        parts.append({"text": bot})
    parts.append({"text": message})

    response = model.generate_content(parts)
    return response.text


gr.ChatInterface(chatbot, type="tuples").launch()

