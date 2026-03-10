from fastapi import FastAPI
from api.routes import invoices, agents, health

app = FastAPI(title="Invoice AI Platform")

app.include_router(invoices.router)
app.include_router(agents.router)
app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "Invoice AI Platform running"}