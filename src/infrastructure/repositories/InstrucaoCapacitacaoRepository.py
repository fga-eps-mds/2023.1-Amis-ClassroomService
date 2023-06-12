from sqlalchemy.orm import Session
from domain.entities.InstrucaoCapacitacao import InstrucaoCapacitacao
from typing import Callable, NoReturn
from domain.repositories import InstrucaoCapacitacaoRepositoryBaseModel


class InstrucaoCapacitacaoRepository:
    database: Callable[[], Session]

    def __init__(self, session: Callable[[], Session]):
        self.database = session

    def save(
        self, instrucaoCapacitacaoSent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao:
        # TODO : verificar se o URM possui isso built in
        session = self.database()
        session.add(instrucaoCapacitacaoSent)
        session.commit()
        session.expunge_all()
        session.close()
        return instrucaoCapacitacaoSent

    def delete_by_id(self, instrucaoId: int) -> NoReturn:
        """Deleta uma instrução de capacitação dado o seu id"""
        session = self.database()

        response = (
            session.query(InstrucaoCapacitacao)
            .filter(InstrucaoCapacitacao.id == instrucaoId)
            .first()
        )

        if response is not None:
            session.delete(response)
            session.commit()

        session.close()


assert isinstance(
    InstrucaoCapacitacaoRepository({}),
    InstrucaoCapacitacaoRepositoryBaseModel.InstrucaoCapacitacaoRepositoryBaseModel,
)
