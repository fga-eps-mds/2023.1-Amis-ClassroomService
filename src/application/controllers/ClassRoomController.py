from sqlalchemy.orm import Session 
from database import get_db 
from database import Base, engine  
from domain.entities.ClassRoom import ClassRoomBase, ClassRoomDB
from domain.entities.ClassRoom import ClassRoomRequest, ClassRoomResponse
from fastapi import APIRouter, status, HTTPException, Form, Depends
from application.useCases.LoginClassRoomUseCase import ClassRoomUseCase
from application.useCases import LoginClassRoomUseCase

from application.controllers import classUseCase

from sqlalchemy import MetaData

Base.metadata.create_all(bind=engine)


router_classRoom = APIRouter(

    prefix = '/classRoom',
    tags = ['classRoom'],
    responses={404: {"description": "Not found"}}

)


@router_classRoom.post("/",status_code=status.HTTP_201_CREATED)
def create_classRoom(class_request: ClassRoomRequest, responde_model:ClassRoomResponse  ,database: Session = Depends(get_db)):
    fieldsValidation = classUseCase.validate_classRoom(class_request)
   
   
   
    class_entitie = ClassRoomDB(**class_request.dict())
    classUseCase.save_class(classSent=class_entitie)

    return class_entitie    

@router_classRoom.get("/")
def find_all_classRoom():
    classRoomDB = classUseCase.find_all_class()
    return classRoomDB 


@router_classRoom.put("/")
async def update_classRoom():
    
    return {"message" : "Atualizado "}


@router_classRoom.delete("/")
async def delete_classRoom():
    
    return {"message" : "Deletado "}