AI‑DUEL
# AI‑Duel — Two AI models enter, one answer leaves
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Backend](https://img.shields.io/badge/Backend-FastAPI-green)
![Status](https://img.shields.io/badge/Project-Skeleton-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
# AI‑Duel — Two AI models enter, one answer leaves  
*A collaborative debate engine for LLMs*

AI‑Duel is an open‑source concept and backend skeleton for a tool where two different language models (e.g., GPT‑4, Gemini, Claude, Groq) are placed into the same “arena” to solve a user‑defined task.

The user provides a single task → both AIs respond → they see each other’s answers → they refine their reasoning → and finally produce a combined, improved answer.

---

## 🔥 What is this?

AI‑Duel is:

- a **debate engine** for two LLMs  
- where the models:
  - answer the task
  - see each other’s responses
  - improve their own answer over several rounds
  - and finally produce a **joint summary**

Goal: combine the strengths of two different models into one superior result.

---
## ✨ Features

- **Two‑model debate loop**  
  Runs a structured back‑and‑forth between two LLMs (Model A vs Model B).

- **Multi‑round refinement**  
  Each model sees the other’s previous answer and improves its own.

- **Final combined answer**  
  After the debate rounds, one model produces a synthesized, improved conclusion.

- **Extensible backend skeleton**  
  Clean FastAPI structure that developers can easily extend with real LLM APIs.

- **Model‑agnostic design**  
  Works with OpenAI, Anthropic, Groq, Google, or any other LLM provider.

- **Simple, hackable architecture**  
  Clear orchestrator logic that anyone can modify or build upon.

- **Open‑source and MIT‑licensed**  
  Free to use, modify, fork, and integrate into other projects.
## 🧠 How it works

1. The user sends to the API:
   - the task (`task`)
   - the model names (`modelA`, `modelB`)
   - number of rounds (`rounds`)

2. The backend:
   - calls both models with the task
   - on the next round, feeds each model the other model’s previous answer
   - repeats this for 2–4 rounds
   - finally asks one model to produce a summary

3. The API returns:
   - round‑by‑round debate history
   - the final combined answer

---

## 📁 Project structure
ai-duel/
├── backend/
│   ├── app.py
│   ├── orchestrator.py
│   └── requirements.txt
└── docs/
└── architecture.md

---

## 🛠 Backend components

### `app.py`
Simple FastAPI HTTP endpoint.

### `orchestrator.py`
The debate loop between two models.

### `requirements.txt`
Python dependencies.

---

## 🚀 How to continue development

This repository is intentionally lightweight so any developer can:

- add real API calls (OpenAI, Google, Anthropic, Groq…)
- build a frontend (React, Svelte, Vue…)
- add model selection UI
- improve the debate loop
- create a visual “AI arena” interface

If you want to continue the project, fork it and go wild.

---

## 📜 License

You may add an MIT License if you want this to be fully open and free.

---

## 💡 Idea

Idea: **Jyrki Järvi (JJ)**  
Implementation: **whoever discovers this repo**
## 🚀 How to run locally

Follow these steps to run the AI‑Duel backend on your own machine.

### 1. Clone the repository
```bash
git clone https://github.com/jyrkijarvi-pixel/ai-duel.git
cd ai-duel/backend
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key_here"      # macOS / Linux
setx OPENAI_API_KEY "your_api_key_here"        # Windows
uvicorn app:app --reload
http://127.0.0.1:8000 (127.0.0.1 in Bing) → health check
http://127.0.0.1:8000/docs (127.0.0.1 in Bing) → interactive API UI (Swagger)
POST /duel
{
  "task": "Explain quantum tunneling",
  "modelA": "gpt-4.1-mini",
  "modelB": "gpt-4.1-mini",
  "rounds": 3
}


