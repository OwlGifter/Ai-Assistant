import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def web_search(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    snippets = []

    for result in results.get("organic_results", [])[:5]:
        title = result.get("title", "")
        snippet = result.get("snippet", "")
        snippets.append(f"{title}: {snippet}")

    return "\n".join(snippets)
