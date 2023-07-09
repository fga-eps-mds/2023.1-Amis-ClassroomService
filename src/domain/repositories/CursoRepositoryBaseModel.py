from domain.entities.Curso import Curso
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class CursoRepositoryBaseModel(Protocol):

    def save(self, class_sent: Curso) -> Curso:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, class_sent: Curso) -> NoReturn:
        """Funçãop para atualizar um Curso, assume que o curso já existe."""
        ...

    def delete_by_id(self, curso_id: int)-> NoReturn:
        '''Função para apagar um curso do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Curso]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        ...
    
    def find_by_id(self, curso_id: int) -> Curso | None:
        """Faz uma busca pelo id e retorna os dados do curso caso existe"""
        ...