from application.useCases.RegisterUseCase import RegisterUseCase
from database import engine, Base
from database import get_db as get_database
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, Response, HTTPException
from src.domain.entities.Register import RegisterRequestId, RegisterResponse, RegisterRequest, Register
from application.useCases.RegisterUseCase import RegisterUseCase
from application.controllers import  registerUseCase


# from application.controllers import registerUseCase
#
#from src.infrastructure.repositories.RegisterRequest import AlunaApiClient

Base.metadata.create_all(bind=engine)


router_register = APIRouter(
    prefix="/register",
    tags=["register"]
)
# # GET ALL
# @router_register.get("/", response_model = list[RegisterResponse])
# def find_all(self,database: Session = Depends(get_database)):
#     '''Faz uma query de todos os objetos register na DB (sem paginação)'''
#     register = RegisterRepository.find_all()
#     return [RegisterResponse.from_orm(register) for register in register]

@router_register.post("/", status_code=status.HTTP_201_CREATED)
def create(register_request: RegisterRequest):

    register_entitie = Register(**register_request.__dict__)

    registerUseCase.save(registerSent=register_entitie)

    return register_request


@router_register.get("/", response_model=list[RegisterResponse])
def find_all():
    '''Faz uma query de todos os objetos register na DB (sem paginação)'''
    register = registerUseCase.find_all()
    return register

# # CONSULTAR VAGAS TOTAIS E PREENCHIDAS NA TURMA BY ID
# @router_register.get("/turma/{codigoTurma}", response_model = {})
# def find_qtd_vagas_by_id(codigoTurma: str, database: Session = Depends(get_database)):
#     '''Dado o ID como parâmetro, retorna a qtd de matricula nessa turma'''

#     turma = RegisterRepository.find_by_id(database, codigoTurma)
#     if not turma:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail = "Turma não encontrada"
#         )
#     print(turma)
#     vagasTotais = turma.capacidade_turma
#     register = len(RegisterRepository.find_by_id(database, codigoTurma))
#     vagasDisponiveis = vagasTotais - register

#     vagas = {
#         "vagasTotais": vagasTotais,
#         "vagasDisponiveis": vagasDisponiveis
#     }

#     return vagas


@router_register.get("/turma/{codigoTurma}",response_model=RegisterResponse,status_code=status.HTTP_200_OK)
def find_by_id(codigoTurma: int):
    '''Faz uma query de um objeto register na DB pelo id'''
    turma = registerUseCase.find_by_id_turma(codigoTurma)

    if turma is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Turna não encontrada")
    print(turma.capacidade_turma)


    vagas={
        "codigoTurma": codigoTurma,  # Verifique se você está passando o valor correto
        "idAluna": 0,  # Verifique se você está passando o valor correto
        "idRegister": 1  # Verifique se você está passando o valor correto
    }

    return vagas

@router_register.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    register = registerUseCase.find_by_id(id)
    if register is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="register não encontrado")

    registerUseCase.delete_by_id(register.idRegister)

    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router_register.put("/{id}", status_code=status.HTTP_201_CREATED)
def update(registerSent: RegisterRequestId):
    if registerUseCase.find_by_id(registerSent.idRegister) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="register não existente")
    registerUseCase.update(registerSent)







"""
@router_register.post("/",
    response_model=list[RegisterResponse],
    status_code=status.HTTP_201_CREATED
)
def create(requests: list[RegisterRequest], database: Session = Depends(get_db)):
    '''Cria e salva uma lista de objetos register por meio do método POST'''
    try:
        new_registers = RegisterUseCase.save(database,requests)
        return new_registers
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(error)
        )
"""



    
# # FIND BY ID
# @router_register.get("/{id}", response_model = {})
# def find_by_id(id: str, database: Session = Depends(get_database)):
#     '''Dado o ID como parâmetro, encontra a matricula com esse ID'''
#     register = RegisterRepository.find_by_id(database, id)

#     if not register:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail = "Register não encontrado"
#         )

#     returnRegister = []

#     api_client = AlunaApiClient()

#     for r in register:
#         AlunaApiClient
#         aluna = api_client.get_aluna(r.id)
#         returnRegister.append(
#             aluna
#         )

#     return returnRegister

# # DELETE BY id
# @router_register.delete("/{codigoTurma}/{idAluna}", status_code = status.HTTP_204_NO_CONTENT)
# def delete_by_id(codigoTurma: str, idAluna: str, database: Session = Depends(get_database)):
#     '''Dado o ID da turma e aluna, deleta o objeto da DB por meio do método DELETE'''
#     if not RegisterRepository.exists_by_id(database, codigoTurma, idAluna):
#         raise HTTPException(
#             status_code = status.HTTP_404_NOT_FOUND, detail="Turma/Aluna não encontrada"
#         )
    
#     Register.delete_by_id(database, codigoTurma, idAluna)
#     return Response(status_code = status.HTTP_204_NO_CONTENT)

# # CONSULTAR VAGAS TOTAIS E PREENCHIDAS NA TURMA BY ID
# @router_register.get("/turma/{codigoTurma}", response_model = {})
# def find_qtd_vagas_by_id(codigoTurma: str, database: Session = Depends(get_database)):
#     '''Dado o ID como parâmetro, retorna a qtd de matricula nessa turma'''

#     turma = RegisterRepository.find_by_id(database, codigoTurma)
#     if not turma:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail = "Turma não encontrada"
#         )
#     print(turma)
#     vagasTotais = turma.capacidade_turma
#     register = len(RegisterRepository.find_by_id(database, codigoTurma))
#     vagasDisponiveis = vagasTotais - register

#     vagas = {
#         "vagasTotais": vagasTotais,
#         "vagasDisponiveis": vagasDisponiveis
#     }

#     return vagas