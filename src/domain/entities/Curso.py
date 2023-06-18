'''Importando parâmetros da orm'''
from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel

class Curso(Base):
    '''Classe para estabelecer o modelo na tabela DB'''
    __tablename__ = "curso"
    __table_args__ = {"extend_existing": True}
    id: int = Column(Integer, primary_key = True, index = True)
    nome : str = Column(String(70), nullable = False)
    descricao : str = Column(String(300), nullable = False)
    duracaoHoras : int= Column(Integer, nullable = False)


class CursoBase(BaseModel):
    nome: str
    descricao: str
    duracaoHoras: int


class CursoRequest(CursoBase):
    '''...'''
    pass

class CursoRequestId(CursoBase):
    """Necessário para se fazer o update"""
    id : int

class CursoResponse(CursoBase):
    '''...'''
    id:int
    class Config:
        orm_mode = True
