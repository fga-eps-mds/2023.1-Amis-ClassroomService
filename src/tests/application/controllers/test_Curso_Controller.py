import pytest
from httpx import AsyncClient
from fastapi import status


GLOBAL_RESPONSE = []
HTTPS_CURSO =  "http://localhost:9090"

@pytest.mark.asyncio
async def test_create_controller():
    data = {
    "nome": "teste",
    "descricao": "um novo teste",
    "duracaoHoras": 2
    }

    async with AsyncClient(base_url=HTTPS_CURSO) as async_client:
        response = await async_client.post("/curso/", json=data)
    assert response.status_code == status.HTTP_201_CREATED


    
@pytest.mark.asyncio
async def test_find_all():
    async with AsyncClient(base_url=HTTPS_CURSO) as async_client:
        response = await async_client.get("/curso/")
    assert response.status_code == status.HTTP_200_OK



@pytest.mark.asyncio
async def test_delete_curso():
    async with AsyncClient(base_url=HTTPS_CURSO) as async_client:
        response = await async_client.delete("/curso/45")





