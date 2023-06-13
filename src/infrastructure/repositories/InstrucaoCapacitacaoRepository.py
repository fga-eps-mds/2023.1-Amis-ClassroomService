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
    ) -> InstrucaoCapacitacao | None:
        # TODO : verificar se o URM possui isso built in
        session = self.database()
        try:
            session.add(instrucaoCapacitacaoSent)
            session.commit()
            session.expunge_all()
            session.close()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()
        return instrucaoCapacitacaoSent

    def update(
        self, instrucaoCapacitacaoSent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao | None:
        session = self.database()
        try:
            session.merge(instrucaoCapacitacaoSent)
            session.commit()
            session.expunge_all()
            session.close()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

        return instrucaoCapacitacaoSent

    def delete_by_id(self, instrucaoId: int) -> None:
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
    
    def find_all(self) -> list[InstrucaoCapacitacao]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        res = session.query(InstrucaoCapacitacao).all()
        session.close()
        return res


assert isinstance(
    InstrucaoCapacitacaoRepository({}),
    InstrucaoCapacitacaoRepositoryBaseModel.InstrucaoCapacitacaoRepositoryBaseModel,
)
