import pytest
from httpx import AsyncClient
from fastapi import status, HTTPException


HTTPS_REGISTER = "http://localhost:9091/"


@pytest.mark.asyncio
async def test_create_Register():
    register = {
        "codigoTurma": 1,
        "idAluna": "pedrohenriqueteste"
     
    }
    async with AsyncClient(base_url=HTTPS_REGISTER) as async_client:
        response = await async_client.post("/register/", json=register)
        print(response)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.asyncio
async def test_find_all_student_controller():
    async with AsyncClient(base_url=HTTPS_REGISTER) as async_client: 
        response = await async_client.get("/register/")
    assert response.status_code == status.HTTP_200_OK
    

""" @pytest.mark.asyncio
async def test_delete_by_id_Register():
    async with AsyncClient(base_url=HTTPS_REGISTER) as async_client:
        response = await async_client.delete("/register/{idRegister}/1/pedrohenriqueteste")
    assert response.status_code == status.HTTP_204_NO_CONTENT

 """
 