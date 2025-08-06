from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="App Service",
    description="App Service",
    version="1.0.0",
)

app.include_router(api_router)
