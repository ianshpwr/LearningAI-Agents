from dotenv import load_dotenv
load_dotenv(override=True)

import os
gemini_api_key = os.getenv('GEMINI_API_KEY')
grok_api_key = os.getenv('GROK_API_KEY')

if gemini_api_key:
    print(f"gemini and grok API Key exists and begins {gemini_api_key[:8]}")
else:
    print("gemini or grok API Key not set - please head to the troubleshooting guide in the setup folder")
    

import google.generativeai as genai
model = genai.GenerativeModel('gemini-1.5-flash')

question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
messages = [{"role": "user", "content": question}]

response  = model.generate_content(question)
question = response.text



messages = [{"role": "user", "content": question}]

response = model.generate_content(contents=messages[0]["content"])
answer = response.text
