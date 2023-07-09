from sqlalchemy.orm import Session
from domain.entities.InstrucaoCapacitacao import InstrucaoCapacitacao
from typing import Callable, NoReturn
from domain.repositories import InstrucaoCapacitacaoRepositoryBaseModel


class InstrucaoCapacitacaoRepository:
    database: Callable[[], Session]

    def __init__(self, session: Callable[[], Session]):
        self.database = session

    def save(
        self, instrucao_capacitacao_sent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao | None:
        # TODO : 
        session = self.database()
        try:
            session.add(instrucao_capacitacao_sent)
            session.commit()
            session.expunge_all()
            session.close()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()
        return instrucao_capacitacao_sent

    def update(
        self, instrucao_capacitacao_sent: InstrucaoCapacitacao
    ) -> InstrucaoCapacitacao | None:
        session = self.database()
        try:
            session.merge(instrucao_capacitacao_sent)
            session.commit()
            session.expunge_all()
            session.close()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

        return instrucao_capacitacao_sent

    def delete_by_id(self, instrucao_id: int) -> None:
        """Deleta uma instrução de capacitação dado o seu id"""
        session = self.database()

        response = (
            session.query(InstrucaoCapacitacao)
            .filter(InstrucaoCapacitacao.id == instrucao_id)
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

    def find_by_id(self, instrucao_capacitacao_id: int) -> InstrucaoCapacitacao | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
16-Arrumando-CodeSmells
        return session.query(InstrucaoCapacitacao).filter(InstrucaoCapacitacao.id == instrucao_capacitacao_id).first()

        return session.query(InstrucaoCapacitacao).filter(InstrucaoCapacitacao.id == instrucaoCapacitacao_id).first()
    
    def find_by_id_curso(self, instrucaoCapacitacao_curso: int) -> list[InstrucaoCapacitacao]:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(InstrucaoCapacitacao).filter(InstrucaoCapacitacao.idCurso == instrucaoCapacitacao_curso).all()


assert isinstance(
    InstrucaoCapacitacaoRepository({}),
    InstrucaoCapacitacaoRepositoryBaseModel.InstrucaoCapacitacaoRepositoryBaseModel,
)
