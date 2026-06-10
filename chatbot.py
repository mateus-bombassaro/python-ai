import os
from google import genai
from dotenv import load_dotenv

load_dotenv() 

gemini_api_key = os.getenv("GEMINI_API_KEY")

print("API Key:", gemini_api_key)
client = genai.Client(api_key=gemini_api_key)

chat = client.chats.create(model="gemini-2.5-flash")

prompt = input("Digite o seu prompt: ")

while prompt != "sair":
  resposta = chat.send_message(prompt)
  print(resposta.text)
  print("\n***\n")
  prompt = input("Digite o seu prompt: ")