from database import engine, Base
from sqlalchemy import Column
from fastapi import APIRouter, status
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
