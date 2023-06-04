'''Importando parâmetros da orm'''
from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 
class CursoBase(BaseModel):
    nome: str
    descricao: str
    duracaoHoras: int

class Curso(Base):
    '''Classe para estabelecer o modelo na tabela DB'''
    __tablename__ = "curso"
    __table_args__ = {"extend_existing": True}
    
    id: int = Column(Integer, primary_key = True, index = True)
    nome : str = Column(String(70), nullable = False)
    descricao : str = Column(String(300), nullable = False)
    duracaoHoras : int= Column(Integer, nullable = False)


class CursoRequest(CursoBase):
    '''...'''
    pass


class CursoResponse(CursoBase):
    
    '''...'''
    id:int
    class Config:
        orm_mode = True

