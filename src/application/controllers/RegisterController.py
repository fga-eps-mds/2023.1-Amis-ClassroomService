from application.useCases.RegisterUseCase import RegisterUseCase
from application.controllers import registerUseCase

from database import engine, Base
from database import get_db as get_database
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, Response, HTTPException
from src.domain.entities.Register import RegisterRequestId, RegisterResponse, RegisterRequest, RegisterDB
from application.useCases.RegisterUseCase import RegisterUseCase

# from application.controllers import registerUseCase
#from src.infrastructure.repositories.RegisterRequest import AlunaApiClient

Base.metadata.create_all(bind=engine)


router_register = APIRouter(
    prefix='/register',
    tags=['register'],
    responses={404 : {"description" : "Not found"}}
)
#  GET ALL

@router_register.post("/", status_code = status.HTTP_201_CREATED)
def create_Register(register_request: RegisterRequest, database : Session = Depends(get_database)):
    register_entitie = RegisterDB(**register_request.dict())
    registerUseCase.save(registerSent=register_entitie)
    return register_request

@router_register.get("/", response_model = list[RegisterResponse])
def find_all(database: Session = Depends(get_database)):
     '''Faz uma query de todos os objetos register na DB (sem paginação)'''
     register = registerUseCase.find_all()
     return [RegisterResponse.from_orm(register) for register in register]

@router_register.get("/{RegisterID}", response_model = RegisterResponse, 
                 status_code = status.HTTP_200_OK)
def find_by_id(register_id : int):
    register = registerUseCase.find_by_id(register_id)

    if not register:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Registro não encontrado"
        )
    return RegisterResponse.from_orm(register)

@router_register.put("/", status_code=status.HTTP_201_CREATED)
def update(registerSent: RegisterRequestId):
    if registerUseCase.find_by_id(registerSent.idRegister) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="register não existente")
    registerUseCase.update(registerSent)

@router_register.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id_Register(register_id : int):
    register = registerUseCase.find_by_id(register_id)

    if register is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Registro não encontrado")
    
    registerUseCase.delete_by_id(register_id=register_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)