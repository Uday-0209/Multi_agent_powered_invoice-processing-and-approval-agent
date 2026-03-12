from fastapi import FastAPI
from api.routes import invoices, agents, health
from dspy_programs.dspy_setup import configure_dspy

app = FastAPI(title="Invoice AI Platform")

configure_dspy()

app.include_router(invoices.router)
app.include_router(agents.router)
app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "Invoice AI Platform running"}