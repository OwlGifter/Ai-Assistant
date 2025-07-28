def needs_web_search(prompt):
    keywords = ["news", "headlines", "latest", "today", "current", "weather", "stock"]
    return any(word in prompt.lower() for word in keywords)
