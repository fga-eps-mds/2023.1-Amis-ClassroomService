from application.useCases.RegisterUseCase import RegisterUseCase
from application.controllers import registerUseCase

from database import engine, Base
from database import get_db as get_database
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, Response, HTTPException
from src.domain.entities.Register import RegisterRequestId, RegisterResponse, RegisterRequest, RegisterDB, RegisterBase, RegisterBaseStudent
from application.useCases.RegisterUseCase import RegisterUseCase

# from application.controllers import registerUseCase
#from src.infrastructure.repositories.RegisterRequest import AlunaApiClient

Base.metadata.create_all(bind=engine)


router_register = APIRouter(
    prefix='/register',
    tags=['register'],
    responses={404 : {"description" : "Not found"}}
)

@router_register.post("/", status_code=status.HTTP_201_CREATED)
def create_Register(register_request: RegisterRequest, database: Session = Depends(get_database)):
    register_entity = RegisterDB(**register_request.__dict__)

    register_sent = register_entity
    ids_aluna = register_sent.idAluna.split(',')
    codigoTurma=register_sent.codigoTurma

    print(type(ids_aluna))
    for id in ids_aluna:
        id_nao_esta_cadastrado_turma=registerUseCase.find_all_student(codigoTurma)
        print(f'O retorno do find: {id_nao_esta_cadastrado_turma}')
        if not any(id in tupla for tupla in id_nao_esta_cadastrado_turma):
            register_sent_copy = RegisterDB(**register_request.__dict__)  # Criar uma nova instância
            register_sent_copy.idAluna = id  # Atribuir o valor correto de id
            registerUseCase.save(register_sent=register_sent_copy)
    
    return register_request


@router_register.get("/", response_model = list[RegisterBase])
def find_by_id():
    register = registerUseCase.find_all() 
    return register

@router_register.get("/{codigoTurma}", response_model = list[RegisterBaseStudent],
                     status_code= status.HTTP_200_OK)
def find_all_student(codigoTurma: int):
    register = registerUseCase.find_all_student(codigoTurma)

    if not register:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Estudantes não encontrados"
        )
    register_responses = []
    
    for idAluna in register:
        register_response = RegisterBaseStudent(idAluna=(idAluna.idAluna))
        register_responses.append(register_response)
    return register_responses


@router_register.put("/{idRegister}", status_code=status.HTTP_201_CREATED)
def update(registerSent: RegisterRequestId):
    if registerUseCase.find_by_id(registerSent.idRegister) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="register não existente")
    registerUseCase.update(registerSent)

@router_register.delete("/{idRegister}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id_Register(register_id : int):
    register = registerUseCase.find_by_id(register_id)

    if register is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Registro não encontrado")
    
    registerUseCase.delete_by_id(register_id=register_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    ####