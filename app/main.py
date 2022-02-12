from typing import Optional
from src.interactive_conditional_samples import interact_model
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(prompt: str) -> str:

    return next(interact_model(prompt))
