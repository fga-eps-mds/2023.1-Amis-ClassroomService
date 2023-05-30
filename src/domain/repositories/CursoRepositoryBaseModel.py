from domain.entities import Curso
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable



@runtime_checkable
class CursoRepositoryBaseModel(Protocol):

    def save(self, database: Session, cursoSent: Curso) -> Curso:
        '''Função para salvar um objeto assistente na DB'''
        ...