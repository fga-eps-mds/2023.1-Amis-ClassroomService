from sqlalchemy.orm import Session 
from database import get_db 
from database import Base, engine    
from domain.entities.Turma import ClassRoomBase, ClassRoomDB
from fastapi import APIRouter, status, HTTPException, Form

Base.metadata.create_all(bind=engine)


router_classRoom = APIRouter(

    prefix = '/classRoom',
    tags = ['classRoom'],
    responses={404: {"description": "Not found"}}

)

""" router_classRoom2 = APIRouter(

    prefix= '/teste',
    tags= ['Turma'],
    responses= {404: {"description": "Not found"}}
)
 """


@router_classRoom.post("/create")
async def create_classRoom():

    return {"message" : "Criado "}


@router_classRoom.get("/find")
async def find_all_classRoom():

    return {"message" : "Listado"}


@router_classRoom.put("/update")
async def update_classRoom():
    
    return {"message" : "Atualizado "}


@router_classRoom.delete("/delete")
async def delete_classRoom():
    
    return {"message" : "Deletado "}