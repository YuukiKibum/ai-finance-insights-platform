from fastapi import FastAPI
from router import router

app = FastAPI(
    title="AI Finance Insights Platform",
    description="Finance insights, risk scoring, and LLM fallback routing",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Finance Insights Platform is running"}
