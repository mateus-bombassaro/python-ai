import os
from google import genai
from dotenv import load_dotenv

load_dotenv() 

gemini_api_key = os.getenv("GEMINI_API_KEY")

print("API Key:", gemini_api_key)
client = genai.Client(api_key=gemini_api_key)

# Gere conteúdo usando o modelo rápido e atual do Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Escreva um haikai sobre programação em Python.",
)

print(response.text)