import os
from dotenv import load_dotenv

load_dotenv() 

groq_api_key = os.getenv("GROQ_API_KEY")
print("GROQ API Key:", groq_api_key)

from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "user",
        "content": "De que é feito o Sol?"
      }
    ],
    temperature=1,
    max_completion_tokens=5000,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")