import pytest
from httpx import AsyncClient
from fastapi import status

GLOBAL_RESPONSE = []
HTTPS_STUDENT = "http://localhost:9091"

# CREATE
@pytest.mark.asyncio
async def test_create_instrucao():
    data = {        
        "idCurso":14,
        "nome": "Plantação",
        "descricao": "Aulas de cultivos",
        "dataCadastro": "2023-01-02",
        "id": 900
    }
    async with AsyncClient(base_url=HTTPS_STUDENT) as async_client:
        response = await async_client.post("/instrucaoCapacitacao/", json=data)
    assert response.status_code == status.HTTP_201_CREATED

# GET ALL
@pytest.mark.asyncio
async def test_read_all_instrucoes():

    async with AsyncClient(base_url=HTTPS_STUDENT) as async_client:
        response = await async_client.get("/instrucaoCapacitacao/")
    assert response.status_code == status.HTTP_200_OK



# DELETE
@pytest.mark.asyncio
async def test_delete_instrucao():
    async with AsyncClient(base_url=HTTPS_STUDENT) as async_client:
        response = await async_client.delete("/instrucaoCapacitacao/900")
    assert response.status_code == status.HTTP_204_NO_CONTENT
