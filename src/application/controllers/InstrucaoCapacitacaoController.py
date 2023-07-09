from database import engine, Base
from fastapi import APIRouter, status, HTTPException, Response
from domain.entities.InstrucaoCapacitacao import (
    InstrucaoCapacitacaoRequest,
    InstrucaoCapacitacao,
    InstrucaoCapacitacaoResponse,
    InstrucaoCapacitacaoRequestId
)
from application.controllers import instrucaoUseCase

Base.metadata.create_all(bind=engine)


router_instrucao = APIRouter(
    prefix="/instrucaoCapacitacao", tags=["instrucaoCapacitacao"]
)


# CREATE
@router_instrucao.post("/", status_code=status.HTTP_201_CREATED)
def create(instrucao_capacitacao_request: InstrucaoCapacitacaoRequest):
    instrucaoCapacitacao_entitie = InstrucaoCapacitacao(
        **instrucao_capacitacao_request.__dict__
    )

    response = instrucaoUseCase.save(
        instrucaoCapacitacaoSent=instrucaoCapacitacao_entitie
    )

    if response is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível salvar a instrução de capacitação",
        )
    return instrucao_capacitacao_request


# READ ALL
@router_instrucao.get("/", response_model=list[InstrucaoCapacitacaoResponse])
def findall():
16-Arrumando-CodeSmells
    instrucao_capacitacao = instrucaoCapacitacaoUseCase.find_all()
    return instrucao_capacitacao

    instrucaoCapacitacao = instrucaoUseCase.find_all()
    return instrucaoCapacitacao




# READ BY ID CURSO
@router_instrucao.get("/curso/{idCurso}", response_model=list[InstrucaoCapacitacaoResponse])
def find_by_id_curso(idCurso: int):
    '''Faz uma query de um objeto instrução na DB pelo id do curso'''
    instrucao_capacitacao = instrucaoUseCase.find_by_id_curso(idCurso)

    if instrucao_capacitacao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instrução não encontrada")

    return instrucao_capacitacao

# READ BY ID
@router_instrucao.get("/{id}",
                  response_model=InstrucaoCapacitacaoResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    instrucao_capacitacao = instrucaoUseCase.find_by_id(id)

    if instrucao_capacitacao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instrução não encontrado")

    return instrucao_capacitacao


# UPDATE
@router_instrucao.put("/{id}", status_code=status.HTTP_201_CREATED)
def update(sent: InstrucaoCapacitacaoRequestId):
    to_save = InstrucaoCapacitacao(**sent.__dict__)
    if instrucaoUseCase.find_by_id(sent.id) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Instrução não existente")
    response = instrucaoUseCase.update(
        instrucaoCapacitacaoSent=to_save)
    if response is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível atualizar a instrução de capacitação",
        )
    

 
    


# DETELE (by id)
@router_instrucao.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_id(id: int):
    """Deleta uma instrução de capacitação dado o seu id"""
    instrucaoUseCase.delete_by_id(instrucaoId=id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)