from sqlalchemy.orm import Session
from domain.entities.InstrucaoCapacitacao import InstrucaoCapacitacao
from typing import Callable
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


assert isinstance(
    InstrucaoCapacitacaoRepository({}),
    InstrucaoCapacitacaoRepositoryBaseModel.InstrucaoCapacitacaoRepositoryBaseModel,
)
