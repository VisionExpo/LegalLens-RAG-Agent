from fastapi import FastAPI
from api.routes import analyze, health, upload

app = FastAPI(title="SamvidAI")

app.include_router(health.router)
app.include_router(upload.router)
app.include_router(analyze.router)
