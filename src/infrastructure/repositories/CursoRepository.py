from sqlalchemy.orm import Session
from domain.entities.Curso import Curso
from typing import Callable
from domain.repositories import CursoRepositoryBaseModel

class CursoRepository:
    
    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, cursoSent: Curso) -> Curso:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        #if self.find_by_login(socialWorkerSent.login):
        #    session.merge(socialWorkerSent)
        #else:
        session.add(cursoSent)
        session.commit()
        session.expunge_all()
        session.close()
        return cursoSent
    
    def find_all(self) -> list[Curso]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        res = session.query(Curso).all()
        session.close()
        return res

assert isinstance(CursoRepository(
    {}), CursoRepositoryBaseModel.CursoRepositoryBaseModel)

    