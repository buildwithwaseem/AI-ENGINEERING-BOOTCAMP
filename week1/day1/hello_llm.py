import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv(dotenv_path=".env copy")

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable not set")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
prompt = "Do you know Dhruv rathee?"
messages = [
    {"role": "user", "content": prompt}
]

response = client.chat.completions.create(model=model, messages=messages)
answer =response.choices[0].message.content
print(answer)