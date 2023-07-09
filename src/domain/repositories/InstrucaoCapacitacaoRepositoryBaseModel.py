from domain.entities.InstrucaoCapacitacao import InstrucaoCapacitacao
from typing import Protocol, runtime_checkable, NoReturn
from sqlalchemy.orm import Session



@runtime_checkable
class InstrucaoCapacitacaoRepositoryBaseModel(Protocol):
    def save(
        self, instrucao_capacitacao_sent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao | None:
        "Salva uma instrução de capacitação no banco de dados"
        ...
    def find_all(self, database: Session) -> list[InstrucaoCapacitacao]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        ...

    def update(
        self, instrucao_capacitacao_sent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao | None:
        "Atualiza uma instrução de capacitação no banco de dados"
        ...

    def delete_by_id(self, instrucao_id: int) -> NoReturn:
        "Deleta uma instrução dado seu ID"
        ...
        
    def find_by_id(self, instrucao_capacitacao_id: int) -> InstrucaoCapacitacao | None:
        ...