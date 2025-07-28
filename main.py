from assistant import ask_openai, web_search, needs_web_search

def main():
    print("Hello! I'm your AI assistant. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if needs_web_search(user_input):
            print("Assistant: Let me check online sources...\n")
            search_results = web_search("today's news")
            response = ask_openai(f"Summarize the following news:\n{search_results}")
        else:
            response = ask_openai(user_input)

        print("Assistant:", response)

if __name__ == "__main__":
    main()
