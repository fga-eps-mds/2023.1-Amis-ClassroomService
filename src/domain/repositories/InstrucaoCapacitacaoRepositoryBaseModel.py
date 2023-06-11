from domain.entities.InstrucaoCapacitacao import InstrucaoCapacitacao
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class InstrucaoCapacitacaoRepositoryBaseModel(Protocol):

    def save(self, instrucaoCapacitacaoSent: InstrucaoCapacitacao) -> InstrucaoCapacitacao:
        '''Função para salvar um objeto assistente na DB'''
        ...


   
