from database import engine, Base
from fastapi import APIRouter, status, HTTPException, Response
from domain.entities.InstrucaoCapacitacao import (
    InstrucaoCapacitacaoRequest,
    InstrucaoCapacitacao,
    InstrucaoCapacitacaoResponse,
)
from application.controllers import instrucaoCapacitacaoUseCase

Base.metadata.create_all(bind=engine)


router_instrucao = APIRouter(
    prefix="/instrucaoCapacitacao", tags=["instrucaoCapacitacao"]
)


# CREATE
@router_instrucao.post("/", status_code=status.HTTP_201_CREATED)
def create(instrucaoCapacitacao_request: InstrucaoCapacitacaoRequest):
    instrucaoCapacitacao_entitie = InstrucaoCapacitacao(
        **instrucaoCapacitacao_request.__dict__
    )

    response = instrucaoCapacitacaoUseCase.save(
        instrucaoCapacitacaoSent=instrucaoCapacitacao_entitie
    )

    if response is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível salvar a instrução de capacitação",
        )
    return instrucaoCapacitacao_request


# READ ALL
@router_instrucao.get("/", response_model=list[InstrucaoCapacitacaoResponse])
def findall():
    instrucaoCapacitacao = instrucaoCapacitacaoUseCase.find_all()
    return instrucaoCapacitacao



# READ BY ID
@router_instrucao.get("/{idCurso}", status_code=status.HTTP_200_OK)
def read_by_id(idCurso: int) -> list[InstrucaoCapacitacaoResponse]:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


# UPDATE
@router_instrucao.put("/{id}", status_code=status.HTTP_201_CREATED)
def update(sent: InstrucaoCapacitacaoRequest):
    # TODO : fazer  tratamento para verificar se o id de fato existe.
    to_save = InstrucaoCapacitacao(**sent.__dict__)
    response = instrucaoCapacitacaoUseCase.update(
        instrucaoCapacitacaoSent=to_save)
    if response is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível atualizar a instrução de capacitação",
        )


# DETELE (by id)
@router_instrucao.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_id(instrucaoId: int):
    """Deleta uma instrução de capacitação dado o seu id"""
    instrucaoCapacitacaoUseCase.delete_by_id(instrucaoId=instrucaoId)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
