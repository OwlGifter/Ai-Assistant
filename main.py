import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load Api key
load_dotenv()
client = OpenAI()  # Automatically picks up your API key from environment

# Basic chatbot loop
def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


def main():
    print("Hello! I'm your AI assistant. Ask me anything. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = ask_openai(user_input)
        print("Assistant:", response)

if __name__ == "__main__":
    main()
