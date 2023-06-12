from domain.entities.InstrucaoCapacitacao import InstrucaoCapacitacao
from typing import Protocol, runtime_checkable, NoReturn


@runtime_checkable
class InstrucaoCapacitacaoRepositoryBaseModel(Protocol):
    def save(
        self, instrucaoCapacitacaoSent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao | None:
        "Salva uma instrução de capacitação no banco de dados"
        ...

    def update(
        self, instrucaoCapacitacaoSent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao | None:
        "Atualiza uma instrução de capacitação no banco de dados"
        ...

    def delete_by_id(self, instrucaoId: int) -> NoReturn:
        "Deleta uma instrução dado seu ID"
        ...
