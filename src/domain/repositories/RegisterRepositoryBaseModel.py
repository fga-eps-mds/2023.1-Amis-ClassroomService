from domain.entities.Register import RegisterDB
from sqlalchemy.orm import Session
from typing import NoReturn, Protocol, runtime_checkable

@runtime_checkable
class RegisterRepositoryBaseModel(Protocol):  
    
    def save(self, database: Session, registerSent: RegisterDB) -> RegisterDB:
        '''Função para salvar um objeto matricula na DB'''
        ...
    
    def update(self, registerSent: RegisterDB) -> NoReturn:
        """Funçãop para atualizar um register, assume que o register já existe."""
        ...

    def find_by_id(self, codigoTurma: int) -> RegisterDB | None:
        """Faz uma busca pelo id e retorna os dados do curso caso existe"""
        ...
    
    def delete_by_id(self, register_id: int)-> NoReturn:
        '''Função para apagar um register do banco pelo id'''
        ...





    # def find_all(self,database: Session) -> list[Register]:
    #     '''Função para fazer uma query de todas as alunas da DB'''
    #     ...
    
    # def find_by_id(self,database: Session, id: str) -> Register:
    #     '''Função para fazer uma query por ID de um objeto Matricula na DB'''
    #     ...
    
    # def exists_by_id(self,database: Session, codigoTurma: int, idAluna: int) -> bool:
    #     '''Função que verifica se a turma e aluna existe pelo ID dado na DB'''
    #     ...
""" 
    def delete_by_id_codigoTurma(self, codigoTurma: int )-> NoReturn:
        ...    
 """    
    # def delete_by_id(self,database: Session, codigoTurma: str, idAluna: str) -> None:
    #     '''Função para excluir uma aluna da turma no DB dado seu ID'''
    #     ...

    