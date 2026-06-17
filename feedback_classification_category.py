

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

# Filtrar positivos:
df_reviews_positivos = df_reviews[df_reviews["sentiment"] == "POSITIVO"]
resenhas_positivas_unidas = "#####".join(df_reviews_positivos["reviewText"].tolist())

# Resposta de categorias
resposta = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=f"""Você é um analista de dados. Vou te passar muitas resenhas positivas de análises
      de um produto e eu quero que você retorne 2 categorias diferentes para os tipos de elogios. 
      Quero que você retorne duas categorias. Aqui estão as resenhas {resenhas_positivas_unidas}. 
      Cada categoria deve ser definida por apenas uma palavra. 
      quero que elas sejam separadas por virgula e em letras minusculas sem acentos.
      Depois, quero que voce retorne APENAS um texto no formato JSON contendo 3 chaves:
      - resenha_original: conteúdo da resenha original em ingles
      - resenha_pt: resenha traduzida para o portugues
      - categoria: categoria da resenha (deve ser uma das categorias que voce criou)
      """
  )

json_format = resposta.text.strip()
print(json_format)


