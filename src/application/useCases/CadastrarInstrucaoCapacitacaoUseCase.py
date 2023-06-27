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
        
    def find_by_id(self, instrucaoCapacitacao_id : int) -> InstrucaoCapacitacaoBase | None:
        return self.__instrucaoCapacitacaoRepository__.find_by_id(instrucaoCapacitacao_id=instrucaoCapacitacao_id)     
    
    def find_by_id_curso(self, id_curso: int) -> list[InstrucaoCapacitacaoResponse]:
        instrucoesCapacitacao_db = self.__instrucaoCapacitacaoRepository__.find_all()  # ou utilize um método específico para buscar por id de curso
        instrucoes_com_curso = []

        for instrucaoCapacitacao_db in instrucoesCapacitacao_db:
            if instrucaoCapacitacao_db.idCurso == id_curso:
                instrucaoCapacitacao = InstrucaoCapacitacaoResponse(
                    idCurso=instrucaoCapacitacao_db.idCurso,
                    id=instrucaoCapacitacao_db.id,
                    nome=instrucaoCapacitacao_db.nome,
                    descricao=instrucaoCapacitacao_db.descricao,
                    dataCadastro=instrucaoCapacitacao_db.dataCadastro
                )
                instrucoes_com_curso.append(instrucaoCapacitacao)
        print(instrucoes_com_curso)
        return instrucoes_com_curso
   

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