from database import engine, Base
from sqlalchemy import Column
from fastapi import APIRouter, status, HTTPException
from domain.entities.InstrucaoCapacitacao import (
    InstrucaoCapacitacaoRequest,
    InstrucaoCapacitacao,
    InstrucaoCapacitacaoResponse,
    NOME_MAX,
    DESCRICAO_MAX,
    DATA_CADASTRO_MAX,
)
from application.controllers import instrucaoCapacitacaoUseCase

Base.metadata.create_all(bind=engine)


router_instrucao = APIRouter(
    prefix="/instrucaoCapacitacao", tags=["instrucaoCapacitacao"]
)


# CREATE
@router_instrucao.post("/", status_code=status.HTTP_201_CREATED)
def create(instrucaoCapacitacao_request: InstrucaoCapacitacaoRequest):
    # Validações
    if len(instrucaoCapacitacao_request.nome) > NOME_MAX:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"O nome deve ter no máximo {NOME_MAX} caracteres",
        )
    if len(instrucaoCapacitacao_request.descricao) > DESCRICAO_MAX:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A descrição deve ter no máximo {DESCRICAO_MAX} caracteres",
        )
    if len(instrucaoCapacitacao_request.dataCadastro) > DATA_CADASTRO_MAX:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A data de cadastro deve ter no máximo {DATA_CADASTRO_MAX} caracteres",
        )

    instrucaoCapacitacao_entitie = InstrucaoCapacitacao(
        **instrucaoCapacitacao_request.__dict__
    )

    instrucaoCapacitacaoUseCase.save(
        instrucaoCapacitacaoSent=instrucaoCapacitacao_entitie
    )

    return instrucaoCapacitacao_request


# READ ALL
@router_instrucao.get("/", status_code=status.HTTP_200_OK)
def read_all() -> list[InstrucaoCapacitacaoResponse]:
    return [
        InstrucaoCapacitacaoResponse(
            idCurso=1,
            id=1,
            nome="nome",
            descricao="descricao",
            dataCadastro="dataCadastro",
        )
    ]


# READ BY ID
@router_instrucao.get("/{idCurso}", status_code=status.HTTP_200_OK)
def read_by_id() -> list[InstrucaoCapacitacaoResponse]:
    return [
        InstrucaoCapacitacaoResponse(
            idCurso=1,
            id=1,
            nome="nome",
            descricao="descricao",
            dataCadastro="dataCadastro",
        )
    ]


# UPDATE
@router_instrucao.post("/update", status_code=status.HTTP_201_CREATED)
def update(instrucaoCapacitacao_sent: InstrucaoCapacitacaoRequest):
    return [
        InstrucaoCapacitacaoResponse(
            idCurso=1,
            id=1,
            nome="nome",
            descricao="descricao",
            dataCadastro="dataCadastro",
        )
    ]


# DETELE (by id)
@router_instrucao.delete("/{idCurso}", status_code=status.HTTP_204_NO_CONTENT)
def delete(idCurso: int):
    pass
