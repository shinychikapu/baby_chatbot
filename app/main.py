from fastapi import FastAPI
from app.api.routes import router as chat_router

app = FastAPI(title="Mom-Baby Chat Agent")

app.include_router(chat_router, prefix="/api")