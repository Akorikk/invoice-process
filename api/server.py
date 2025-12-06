# api/server.py

from fastapi import FastAPI
from api.human_review import router as human_router

app = FastAPI(title="Invoice Workflow HITL API")

app.include_router(human_router)


@app.get("/")
def root():
    return {"message": "Invoice Workflow HITL API Running"}
