from sqlalchemy.orm import Session
from domain.entities.Curso import Curso
from typing import Callable
from domain.repositories import CursoRepositoryBaseModel
from typing import NoReturn

class CursoRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, cursoSent: Curso) -> Curso:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(cursoSent)
        session.commit()
        session.expunge_all()
        session.close()
        return cursoSent

    def update(self, cursoSent: Curso) -> NoReturn:
        session = self.database()
        session.merge(cursoSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Curso]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        res = session.query(Curso).all()
        session.close()
        return res

    def delete_by_id(self, curso_id: int) -> NoReturn:
        """Função para deletar um curso do DB, caso exista"""
        session = self.database()
        curso_session = session.query(Curso).filter(Curso.id == curso_id).first()

        if curso_session is not None:
            session.delete(curso_session)
            session.commit()

        session.close()

    def find_by_id(self, curso_id: int) -> Curso | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Curso).filter(Curso.id == curso_id).first()

assert isinstance(CursoRepository(
    {}), CursoRepositoryBaseModel.CursoRepositoryBaseModel)
