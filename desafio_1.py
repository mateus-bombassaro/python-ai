import os
from google import genai
from dotenv import load_dotenv
from email_templates import emails_corpo 
import pandas as pd

load_dotenv() 

gemini_api_key = os.getenv("GEMINI_API_KEY")

print("API Key:", gemini_api_key)
client = genai.Client(api_key=gemini_api_key)


# Etapa 1 - criar perguntas e escrever arquivo

lista_de_perguntas = [
  "De que é feito o sol?",
  "De que é feito o planeta Saturno?",
  "Qual é a galáxia mais antiga?",
  "Qual é a maior estrela já encontrada?",
]

with open("perguntas.txt", "w", encoding="utf-8") as file:
  for pergunta in lista_de_perguntas:
    file.write(pergunta + "\n")

# Etapa 2 - ler perguntas
lista_desafio = []

with open("perguntas.txt", "r", encoding="utf-8") as file:
  for linha in file:
    pergunta = linha.strip()
    lista_desafio.append(pergunta)

# Etapa 3 - usar LLM para responder perguntas
lista_de_dicionarios_de_respostas = []

for pergunta in lista_desafio:
  resposta = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Gere uma resposta muito sucinta para a seguinte pergunta: {pergunta}"
  )
  lista_de_dicionarios_de_respostas.append({"pergunta": pergunta, "resposta": resposta.text})

#Etapa 4 - escrever respostas e perguntas num arquivo

with open("respostas_1.csv", "w", encoding="utf-8") as file:
  file.write("Pergunta,Resposta\n")
  for item in lista_de_dicionarios_de_respostas:
    file.write(f"{item['pergunta']},{item['resposta']}\n") 

#Etapa 4.1 - escrever respostas e perguntas num arquivo usando pandas

df_perguntas_respostas = pd.DataFrame(lista_de_dicionarios_de_respostas)
df_perguntas_respostas.to_csv("respostas_2.csv", index=False, encoding="utf-8")