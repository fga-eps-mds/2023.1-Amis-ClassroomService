import pytest
from httpx import AsyncClient
from fastapi import status

GLOBAL_RESPONSE = []
HTTPS_STUDENT = "http://localhost:9091"

#CREATE
@pytest.mark.asyncio
async def test_create_classroom():
    data = {
    "codigo": 1,
    "nome_turma": "Teste",
    "data_inicio": "2000-09-02",
    "data_fim": "2000-09-02",
    "inicio_aula": "10:00",
    "fim_aula": "10:00",
    "capacidade_turma": 20,
    "fk_curso": 0,
    "fk_professor": "login",
    "descricao": "string"
    }
    async with AsyncClient(base_url=HTTPS_STUDENT) as async_client:
        response = await async_client.post("/classRoom/", json=data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
async def test_find_all():

    async with AsyncClient(base_url = HTTPS_STUDENT) as async_client:
        response = await async_client.get("/classRoom/")
    assert response.status_code == status.HTTP_200_OK    



@pytest.mark.asyncio
async def test_delete_classroom():
        
    async with AsyncClient (base_url=HTTPS_STUDENT) as async_client:
        response = await async_client.delete("/classRoom/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT