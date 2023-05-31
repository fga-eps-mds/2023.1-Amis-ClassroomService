from domain.entities.Curso import Curso
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable



@runtime_checkable
class CursoRepositoryBaseModel(Protocol):

    def save(self, database: Session, cursoSent: Curso) -> Curso:
        '''Função para salvar um objeto assistente na DB'''
        ...
    def find_all(self, database: Session) -> list[Curso]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''