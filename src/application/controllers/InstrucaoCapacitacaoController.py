from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from domain.entities.InstrucaoCapacitacao import (InstrucaoCapacitacaoRequest, InstrucaoCapacitacao)
from application.controllers import  instrucaoCapacitacaoUseCase

Base.metadata.create_all(bind=engine)


router_instrucao = APIRouter(
    prefix="/instrucaoCapacitacao",
    tags=["instrucaoCapacitacao"]
)



@router_instrucao.post("/", status_code=status.HTTP_201_CREATED)
def create(instrucaoCapacitacao_request: InstrucaoCapacitacaoRequest):

    instrucaoCapacitacao_entitie = InstrucaoCapacitacao(**instrucaoCapacitacao_request.__dict__)

    instrucaoCapacitacaoUseCase.save(instrucaoCapacitacaoSent=instrucaoCapacitacao_entitie)

    return instrucaoCapacitacao_request




