# 1. Carregar arquivo txt onde cada linha será o elemento de uma lista
# 2. mandar para modelo local para extrair em formato JSON onde cada item terá usuario, resenha_original, resenha_pt e avaliacao
# 3. Transformar a resposta do modelo em uma lista de dicionarios
# 4. Criar uma funçao que dada uma lista de dicionarios percorre a lista e faz 2 coisas:
#    a. Conta a quantidade de avaliações positivas, negativas e neutras
#    b. Une cada item dessa lista em uma variável do tipo string com algum separador
# 5. Ao final a função retorna tudo

import json
from llm_client import getLLMResponse 
review_list = []

# Etapa 1
with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as file:
  for line in file:
    review_list.append(line.strip())


# Etapa 2 e 3
review_dict_list = []
for index, review in enumerate(review_list):
  print(f"Processing: {index + 1}/{len(review_list)}")
  response = getLLMResponse(review)
  response_json = response.choices[0].message.content
  review_dict_list.append(json.loads(response_json.replace("```json", '').replace("```", '')))
 
#Etapa 4
def count_and_join(dict_list):
  count_positive = 0
  count_negative = 0
  count_neutral = 0
  joined_reviews = []

  for review in dict_list:
    if review.get("avaliacao") is None:
      print(f"Avaliação ausente para a resenha: {review.get('resenha_original', 'Resenha original ausente')}")
      break
    if review["avaliacao"] == "Positiva":
      count_positive += 1
    elif review["avaliacao"] == "Negativa":
      count_negative += 1
    elif review["avaliacao"] == "Neutra":
      count_neutral += 1
    
    joined_reviews.append(str(review))

  joined_reviews = "#####".join(joined_reviews)

  return count_positive, count_negative, count_neutral, joined_reviews
  
pos, neg, neu, joined = count_and_join(review_dict_list)
print(f"Positivas: {pos}, Negativas: {neg}, Neutras: {neu}")
print(joined)
