from openai import OpenAI

client_openai = OpenAI(
  base_url="http://127.0.0.1:1234/v1",
  api_key="FAKE_KEY"
)

def getLLMResponse(review):
  return client_openai.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[
      {
        "role": "system",
        "content": """Você é um especialista em análise de dados e conversão de dados para JSON.
        Você receberá uma linha de texto que é uma resenha de aplicativo de um marketplace online.
        Eu quero que você analise a resenha e retorne um JSON com as seguintes chaves (e apenas essas chaves):
         - usuario: nome do usuário que fez a resenha
         - resenha_original: conteúdo da resenha original no idioma original
         - resenha_pt: resenha traduzida para o portugues brasileiro. Deve estar sempre na lingua portuguesa (brasil)
         - avaliacao: classificacao 'Positiva', 'Negativa' ou 'Neutra' da resenha. Apenas uma palavra. 
         
         Regra importante: Deve retornar apenas o JSON, sem nenhum texto adicional."""
      },
      {
        "role": "user",
        "content": f"Aqui está a resenha: {review}"
      }
    ],
    temperature=0.0,
  )
