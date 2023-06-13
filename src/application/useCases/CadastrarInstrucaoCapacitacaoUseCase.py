from domain.entities.InstrucaoCapacitacao import (
    InstrucaoCapacitacao,
    InstrucaoCapacitacaoResponse
)
from domain.repositories.InstrucaoCapacitacaoRepositoryBaseModel import (
    InstrucaoCapacitacaoRepositoryBaseModel,
)
from typing import NoReturn


class InstrucaoCapacitacaoUseCase:
    __instrucaoCapacitacaoRepository__: InstrucaoCapacitacaoRepositoryBaseModel

    def __init__(
        self, instrucaoCapacitacaoRepository: InstrucaoCapacitacaoRepositoryBaseModel
    ):
        self.__instrucaoCapacitacaoRepository__ = instrucaoCapacitacaoRepository

    def save(
        self, instrucaoCapacitacaoSent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao:
        """Salva uma instrução de capacitação no banco de dados"""
        return self.__instrucaoCapacitacaoRepository__.save(
            instrucaoCapacitacaoSent=instrucaoCapacitacaoSent
        )

    def update(
        self, instrucaoCapacitacaoSent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao:
        """Atualiza uma instrução de capacitação no banco de dados"""
        return self.__instrucaoCapacitacaoRepository__.update(
            instrucaoCapacitacaoSent=instrucaoCapacitacaoSent
        )

    def delete_by_id(self, instrucaoId: int) -> NoReturn:
        """Deleta uma instrução de capacitação no banco de dados,
        dado seu id"""
        self.__instrucaoCapacitacaoRepository__.delete_by_id(
            instrucaoId=instrucaoId)

    def find_all(self) -> list[InstrucaoCapacitacaoResponse]:
        instrucoesCapacitacao_db = self.__instrucaoCapacitacaoRepository__.find_all()
        instrucoesCapacitacao = []
        for instrucaoCapacitacao_db in instrucoesCapacitacao_db:
            instrucaoCapacitacao = InstrucaoCapacitacaoResponse(
                idCurso=instrucaoCapacitacao_db.idCurso,
                id=instrucaoCapacitacao_db.id,
                nome=instrucaoCapacitacao_db.nome,
                descricao=instrucaoCapacitacao_db.descricao,
                dataCadastro=instrucaoCapacitacao_db.dataCadastro
            )
            instrucoesCapacitacao.append(instrucaoCapacitacao)
        return instrucoesCapacitacao