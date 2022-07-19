from fastapi import FastAPI
from enum import Enum

app = FastAPI()

usersDB = [
    {"id": 1},
    {"id": 2},
    {"id": 3}
]

@app.get("/")
async def func():
    return {
        "homepage": "Hello World"
    }


@app.get("/users")
async def func(
    skip: int = 0
    ):
    return {
        "users": usersDB[skip:]
    }