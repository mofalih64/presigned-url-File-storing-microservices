from fastapi import FastAPI
from app.api.router import api_router
from fastapi.staticfiles import StaticFiles
from app.core.config import settings

app = FastAPI(
    title="App Service",
    description="App Service",
    version="1.0.0",
)

# Serve files from /static at /static/*
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

app.include_router(api_router)
