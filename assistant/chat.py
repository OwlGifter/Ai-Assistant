import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
