from dotenv import load_dotenv
load_dotenv(override=True)

import os
gemini_api_key = os.getenv('GEMINI_API_KEY')
grok_api_key = os.getenv('GROK_API_KEY')

if gemini_api_key and grok_api_ley:
    print(f"gemini and grok API Key exists and begins {gemini_api_key[:8]} and {grok_api_ley[:8]}")
else:
    print("gemini or grok API Key not set - please head to the troubleshooting guide in the setup folder")
    
