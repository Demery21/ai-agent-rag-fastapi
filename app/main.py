from fastapi import FastAPI
from agent import run_agent

app = FastAPI(title="AI Agent with RAG")

@app.post("/ask")
async def ask_agent(query: str):
    response = run_agent(query)
    return {"answer": response}
