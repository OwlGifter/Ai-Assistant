# Ai-Assistant
This project will be a small API based Ai assistant

Since it is a small personal project the following are future plans and what i have already completed:

Ai Assistant Development Roadmap/ Plan

---
✅ Phase 1: MVP(Minimum Viable Product)

✔️ Command-line tool with Python

Simple assistant that responds in the terminal via GPT
“Just works” version. Command-line or web-based interface.

Core Features:
- Text input/output (basic chatbot style) - complete(console)
- Integrate OpenAI’s API (ChatGPT-like responses) - complete(connected to gpt3.5-turbo)
- Handle basic commands:
- Search the web - complete (if detects needed websearch, looks up inquiry on google and parses data)
- Get the weather - 
- Fetch calendar events (Google Calendar)
- To-do list (stored locally or in a file)
---

🧠 Phase 2: Smarter, More Useful

🛠 We'll build features into this

Add voice, custom commands, weather, file reading, memory

Give it more capabilities using APIs and tools.

Additions:
- Voice input/output (using SpeechRecognition and pyttsx3 or ElevenLabs)
- File summarization (upload a PDF or doc)
- Summarize your emails (Gmail API)
- Code interpreter (run simple Python code or math problems)
- Save context / memory (use a vector DB like Chroma or just a JSON file for now)

---
🌐 Phase 3: GUI – Web App or Desktop App

❓ Optional for later

Optional web or desktop app (Flask/React/electron, etc.)

Turn it into something more user-friendly and portable:

- Build a React frontend (or use Streamlit for easier setup)
- Host it (e.g., on Render, Heroku, or locally via Docker)
- Make it look like Jarvis 😄
