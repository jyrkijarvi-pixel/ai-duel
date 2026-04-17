# AI‑Duel – Architecture Overview

AI‑Duel is a lightweight backend skeleton designed to run a multi‑round debate between two language models.  
The architecture is intentionally simple so developers can extend it freely.

---

## 🧱 High‑level structure
ai-duel/
├── backend/
│   ├── app.py
│   ├── orchestrator.py
│   └── requirements.txt
└── docs/
└── architecture.md
---

## ⚙️ Components

### 1. `app.py` — FastAPI backend
- Exposes two endpoints:
  - `GET /` → health check
  - `POST /duel` → runs the debate
- Calls `run_debate()` from `orchestrator.py`

### 2. `orchestrator.py` — Debate engine
- Handles the multi‑round debate loop
- Each round:
  - Model A sees Model B:n edellinen vastaus
  - Model B sees Model A:n edellinen vastaus
  - Molemmat parantavat omaa vastaustaan
- Lopuksi pyydetään yhteenveto yhdeltä mallilta

### 3. `requirements.txt`
- Minimiriippuvuudet:
  - FastAPI
  - Uvicorn

---

## 🔄 Data flow

1. **Client** lähettää:
   - task
   - modelA
   - modelB
   - rounds

2. **FastAPI (`app.py`)** vastaanottaa pyynnön  
   → kutsuu `run_debate()`

3. **Orchestrator**:
   - suorittaa kierrokset
   - tallentaa historian
   - tuottaa lopullisen vastauksen

4. **API** palauttaa:
   - kierroskohtaisen historian
   - lopullisen yhdistetyn vastauksen

---

## 🚀 Extending the system

Developers can easily add:

- oikeat LLM‑kutsut (OpenAI, Anthropic, Google, Groq…)
- frontend (React / Svelte / Vue)
- model‑valintakomponentti
- visuaalinen “AI arena” UI
- parempi debattilogiikka
- tallennus tietokantaan

---

## 🎯 Design philosophy

- Keep it simple  
- Make it hackable  
- Let developers extend it freely  
- Provide a clear debate loop that anyone can build on

---

## 💡 Idea origin

Concept: **Jyrki Järvi (JJ)**  
Implementation: **whoever discovers this repo**
