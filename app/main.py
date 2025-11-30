from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from . import models
from .routes import users, todos

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GrowEasy Todo API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:19006",
        "http://127.0.0.1:19006",
        "http://localhost:8081",
        "http://127.0.0.1:8081",
        "*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return {"message": "pong"}


app.include_router(users.router)
app.include_router(todos.router)
