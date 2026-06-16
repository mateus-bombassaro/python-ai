#Desafio:
#1 carregar arquivo .csv com feedback de clientes, 
#2 usar um LLM para classificar o sentimento de cada feedback (POSITIVO, NEGATIVO, NEUTRO)
#3 adicionar essa classificacao ao dataframe

import os
from google import genai
from dotenv import load_dotenv
from email_templates import emails_corpo 
import pandas as pd

load_dotenv() 

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api_key)

#Etapa 1
df_reviews = pd.read_csv("reviews.csv")

#Etapa 2 e 3
for review_number, review in enumerate(df_reviews["reviewText"]):
  resposta = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=f"""Classifique o sentimento do seguinte feedback de cliente como POSITIVO, NEGATIVO ou NEUTRO: {review}. Retorne apenas uma palavra com a classificação do sentimento."""
  )
  df_reviews.loc[review_number, "sentiment"] = resposta.text.strip()
  print(f"Review {review_number + 1}: {resposta.text.strip()}")

print(df_reviews.head())

print ("-" * 50)

