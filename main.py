from typing import Optional
from json import loads
from fastapi import Body, FastAPI, Request

from types_model import ChallengePayload

app = FastAPI()


async def handle_challenge(body: Body) -> ChallengePayload:
    try:
        load = loads(await body())
        if load and load.get("challenge"):
            return ChallengePayload(load)
    except:
        return None


@app.middleware("http")
async def challenge_middleware(request: Request, call_next):
    challenge_result = await handle_challenge(request.body)

    print("challenge_result:", challenge_result)

    if not challenge_result:
        print("return None, no handle_challenge action")
        # return None

    response = await call_next(request)
    return response


@app.get("/")
def home():
    return {"message": "hello world"}


@app.post("/handle_challenge")
def handle_create_item(body = Body(...)):
    print("this is item:", body)

# @app.delete("/items/{item_id}")
# def delelte_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

