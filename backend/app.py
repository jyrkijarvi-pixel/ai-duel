
from fastapi import FastAPI
from orchestrator import run_debate

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI-Duel backend is running"}

@app.post("/duel")
def duel(task: str, modelA: str, modelB: str, rounds: int = 3):
    """
    Start a debate between two language models.
    """
    result = run_debate(task, modelA, modelB, rounds)
    return result
