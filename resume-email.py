import os
from google import genai
from dotenv import load_dotenv
from email_templates import emails_corpo 

load_dotenv() 

gemini_api_key = os.getenv("GEMINI_API_KEY")

print("API Key:", gemini_api_key)
client = genai.Client(api_key=gemini_api_key)

def email_resume(emails_list): 
  for numero, email in enumerate(emails_list):
    resposta = client.models.generate_content(
      model="gemini-2.5-flash",
      contents=f"""Vou te mandar o corpo de um email, quero que você o 
        resuma em apenas 1 linha, segue o email: {email}"""
      )
    print(f"Email {numero + 1}: {resposta.text}")
    print("-" * 50)

email_resume(emails_corpo)