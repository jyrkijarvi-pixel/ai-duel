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

