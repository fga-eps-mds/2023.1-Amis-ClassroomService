from sqlalchemy.orm import Session 
from database import get_db 
from database import Base, engine  
from domain.entities.ClassRoom import ClassRoomBase, ClassRoomDB
from domain.entities.ClassRoom import ClassRoomRequest, ClassRoomResponse , ClassRoomRequestCodigo
from fastapi import APIRouter, status, HTTPException, Form, Depends, Response
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

#Funfando
@router_classRoom.post("/", status_code=status.HTTP_201_CREATED)
def create_classRoom(class_request: ClassRoomRequest ,database: Session = Depends(get_db)):
    fieldsValidation = classUseCase.validate_classRoom(class_request)
   
    class_entitie = ClassRoomDB(**class_request.dict())
    classUseCase.save_class(classSent=class_entitie)

    return class_request    

## Funfando
@router_classRoom.get("/", response_model= list[ClassRoomBase])
def find_all_classRoom():
    classRoomFind = classUseCase.find_all_class()
    return classRoomFind


##Funfando
@router_classRoom.get("/{codigo}",response_model= ClassRoomResponse, status_code= status.HTTP_200_OK)
def find_classRoom_codigo(codigo : int ):
    classRoom = classUseCase.find_classRoom_codigo(codigo)
    
    if not classRoom:
        raise HTTPException(
            statusCode= status.HTTP_404_NOT_FOUND, detail = "Turma não encontrada"
        )
    
    return ClassRoomResponse.from_orm(classRoom) 


@router_classRoom.put("/{codigo}", status_code=status.HTTP_201_CREATED)
def update_classRoom(classSent : ClassRoomRequestCodigo):
    if classUseCase.find_classRoom_codigo(classSent.codigo) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 
                            detail = "Turma não encontrada")
    classUseCase.update_classRoom(classSent)



@router_classRoom.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_classRoom_codigo(codigo:int):
    classRoom = classUseCase.find_classRoom_codigo(codigo)
    if classRoom is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Turma não encontrada" )
    
    classUseCase.delete_classRoom_codigo(codigo=codigo)
    return Response(status_code=status.HTTP_204_NO_CONTENT)