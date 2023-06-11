from domain.entities.InstrucaoCapacitacao import InstrucaoCapacitacao, InstrucaoCapacitacaoRequest, InstrucaoCapacitacaoBase, InstrucaoCapacitacaoRequestId
from domain.repositories.InstrucaoCapacitacaoRepositoryBaseModel import InstrucaoCapacitacaoRepositoryBaseModel
from typing import NoReturn

class InstrucaoCapacitacaoUseCase():
    __instrucaoCapacitacaoRepository__: InstrucaoCapacitacaoRepositoryBaseModel

    def __init__(
        self,
        instrucaoCapacitacaoRepository: InstrucaoCapacitacaoRepositoryBaseModel
    ):
        self.__instrucaoCapacitacaoRepository__ = instrucaoCapacitacaoRepository

    def save(self, instrucaoCapacitacaoSent: InstrucaoCapacitacao) -> InstrucaoCapacitacao:
        '''Função para salvar um objeto SocialWorker na DB, utilizada também como update'''
        return self.__instrucaoCapacitacaoRepository__.save(instrucaoCapacitacaoSent=instrucaoCapacitacaoSent)

    