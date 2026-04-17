
from typing import List, Dict

def call_model(model_name: str, prompt: str) -> str:
    """
    Placeholder for calling a real LLM API.
    Replace this with actual API calls (OpenAI, Anthropic, Google, Groq...).
    """
    return f"[{model_name} response to]: {prompt}"


def run_debate(task: str, modelA: str, modelB: str, rounds: int = 3) -> Dict:
    """
    Runs a multi-round debate between two language models.
    Each model sees the other's previous answer and refines its own.
    """
    history: List[Dict] = []

    prevA = call_model(modelA, task)
    prevB = call_model(modelB, task)

    history.append({
        "round": 1,
        "modelA": prevA,
        "modelB": prevB
    })

    for r in range(2, rounds + 1):
        promptA = f"Task: {task}\nOther model's answer: {prevB}\nRefine your answer."
        promptB = f"Task: {task}\nOther model's answer: {prevA}\nRefine your answer."

        prevA = call_model(modelA, promptA)
        prevB = call_model(modelB, promptB)

        history.append({
            "round": r,
            "modelA": prevA,
            "modelB": prevB
        })

    # Final combined answer
    summary_prompt = (
        f"Task: {task}\n\n"
        f"Model A final answer: {prevA}\n"
        f"Model B final answer: {prevB}\n\n"
        "Produce a combined, improved summary."
    )

    final_answer = call_model(modelA, summary_prompt)

    return {
        "history": history,
        "final_answer": final_answer
    }
