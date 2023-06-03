from sqlalchemy.orm import Session 
from database import get_db 
from database import Base, engine  
from domain.entities.ClassRoom import ClassRoomBase, ClassRoomDB
from domain.entities.ClassRoom import ClassRoomRequest, ClassRoomResponse
from fastapi import APIRouter, status, HTTPException, Form, Depends
from application.useCases.LoginClassRoom import ClassRoomUseCase
from application.useCases import LoginClassRoom

from application.controllers import classUseCase

Base.metadata.create_all(bind=engine)


router_classRoom = APIRouter(

    prefix = '/classRoom',
    tags = ['classRoom'],
    responses={404: {"description": "Not found"}}

)


@router_classRoom.post("/",status_code=status.HTTP_201_CREATED)
def create_classRoom(class_request: ClassRoomRequest, database: Session = Depends(get_db)):
    
    class_entitie = ClassRoomDB(**class_request.dict())
    classUseCase.save_class(classSent=class_entitie)

    return class_entitie    


@router_classRoom.get("/")
def find_all_classRoom():

    return {"message": "Listado "}


@router_classRoom.put("/update")
async def update_classRoom():
    
    return {"message" : "Atualizado "}


@router_classRoom.delete("/delete")
async def delete_classRoom():
    
    return {"message" : "Deletado "}