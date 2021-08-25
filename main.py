from typing import Optional
from json import loads
from fastapi import Body, FastAPI, Request
import re
from types_model import ChallengePayload

app = FastAPI()


def handle_challenge(payload):
    print("--------------------")
    print(payload)
    # decode here
    print("--------------------")
    breakpoint()
        


@app.middleware("http")
async def challenge_middleware(request: Request, call_next):
    # data = request.json()
    # breakpoint()
    payload = await request.body()
    challenge_result = handle_challenge(payload)

    response = await call_next(request)
    return response


@app.get("/")
def home_get():
    print("home_get:")
    # breakpoint()
    return {"message": "hello world"}


@app.post("/")
def home_post(body=Body(...)):
    # breakpoint()
    # load_str = body.decode("utf-8")
    challenge = str(body)
    print("challenge:", challenge)
    return challenge





