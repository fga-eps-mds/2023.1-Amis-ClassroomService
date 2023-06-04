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


@router_classRoom.post("/", status_code=status.HTTP_201_CREATED)
def create_classRoom(class_request: ClassRoomRequest ,database: Session = Depends(get_db)):
    fieldsValidation = classUseCase.validate_classRoom(class_request)
   
    class_entitie = ClassRoomDB(**class_request.dict())
    classUseCase.save_class(classSent=class_entitie)

    return class_request    


@router_classRoom.get("/", response_model= list[ClassRoomBase])
def find_all_classRoom():
    classRoomFind = classUseCase.find_all_class()
    return classRoomFind


@router_classRoom.get("/",response_model= ClassRoomResponse, status_code= status.HTTP_200_OK)
def find_classRoom_codigo(codigo : int ):
    classRoom = classUseCase.find_classRoom_codigo(codigo)
    
    if not classRoom:
        raise HTTPException(
            statusCode= status.HTTP_404_NOT_FOUND, detail = "Turma não encontrada"
        )
    
    return ClassRoomResponse.from_orm(classRoom)

@router_classRoom.put("/")
def update_classRoom():
    return {"mds"}


@router_classRoom.delete("/")
def delete_classRoom():
    
    return {"message" : "Deletado "}