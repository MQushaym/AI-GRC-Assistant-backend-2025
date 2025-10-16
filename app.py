from fastapi import FastAPI, Request
from rag_system import RAGSystem

app = FastAPI()

rag = RAGSystem(vector_db_path="vector_db")
rag.load_vectorstore()
rag.load_llm()
rag.get_prompt_template()

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question")
    if not question:
        return {"error": "Question is required"}
    answer = rag.ask_question(question)
    return {"answer": answer}
