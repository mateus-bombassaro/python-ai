from openai import OpenAI

client_openai = OpenAI(
  base_url="http://127.0.0.1:1234/v1",
  api_key="FAKE_KEY"
)

llm_response = client_openai.chat.completions.create(
  model="google/gemma-3-1b",
  messages=[
    {
      "role": "system",
      "content": "Você é um assistente de IA que sempre responde de forma sarcastica"
    },
    {
      "role": "user",
      "content": "Qual é a capital da França?"
    }
  ],
  temperature=1.0,
)

print(llm_response)

print("-" * 50)

print(llm_response.choices[0].message.content)