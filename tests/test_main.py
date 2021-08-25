# from main import
from json import dumps
import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_home():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "hello world"}


@pytest.mark.asyncio
async def test_handle_challenge_middleware():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        body = {"challenge": "1234567890"}
        headers = {"content-type": "application/json"}
        dumps_body = dumps(body)
        response = await ac.post("/", data=dumps_body, headers=headers)
        assert response.status_code == 200
        assert response.json() == body

        response = await ac.post("/create-item", data=dumps_body, headers=headers)
        assert response.status_code == 200
        assert response.json() == body