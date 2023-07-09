from domain.entities.InstrucaoCapacitacao import (
    InstrucaoCapacitacao,
    InstrucaoCapacitacaoResponse,
    InstrucaoCapacitacaoBase
)
from domain.repositories.InstrucaoCapacitacaoRepositoryBaseModel import (
    InstrucaoCapacitacaoRepositoryBaseModel,
)
from typing import NoReturn


class InstrucaoCapacitacaoUseCase:
    __instrucao_capacitacao_repository__: InstrucaoCapacitacaoRepositoryBaseModel

    def __init__(
        self, instrucaoCapacitacaoRepository: InstrucaoCapacitacaoRepositoryBaseModel
    ):
        self.__instrucaoCapacitacaoRepository__ = instrucaoCapacitacaoRepository

    def save(
        self, instrucao_capacitacao_sent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao:
        """Salva uma instrução de capacitação no banco de dados"""
        return self.__instrucaoCapacitacaoRepository__.save(
            instrucaoCapacitacaoSent=instrucao_capacitacao_sent
        )

    def update(
        self, instrucao_capacitacao_sent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao:
        """Atualiza uma instrução de capacitação no banco de dados"""
        return self.__instrucaoCapacitacaoRepository__.update(
            instrucaoCapacitacaoSent=instrucao_capacitacao_sent
        )

    def delete_by_id(self, instrucao_id: int) -> NoReturn:
        """Deleta uma instrução de capacitação no banco de dados,
        dado seu id"""
        self.__instrucaoCapacitacaoRepository__.delete_by_id(
            instrucaoId=instrucao_id)
        
    def find_by_id(self, instrucao_capacitacao_id : int) -> InstrucaoCapacitacaoBase | None:
        return self.__instrucaoCapacitacaoRepository__.find_by_id(instrucao_capacitacao_id=instrucao_capacitacao_id)   

    def find_all(self) -> list[InstrucaoCapacitacaoResponse]:
        instrucoesCapacitacao_db = self.__instrucaoCapacitacaoRepository__.find_all()
        instrucoesCapacitacao = []
        for instrucao_capacitacao_db in instrucoesCapacitacao_db:
            instrucao_capacitacao = InstrucaoCapacitacaoResponse(
                idCurso=instrucao_capacitacao_db.idCurso,
                id=instrucao_capacitacao_db.id,
                nome=instrucao_capacitacao_db.nome,
                descricao=instrucao_capacitacao_db.descricao,
                dataCadastro=instrucao_capacitacao_db.dataCadastro
            )
            instrucoesCapacitacao.append(instrucao_capacitacao)
        return instrucoesCapacitacao