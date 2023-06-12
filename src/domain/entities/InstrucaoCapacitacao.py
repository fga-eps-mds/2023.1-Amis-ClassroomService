'''Importando parâmetros da orm'''
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from pydantic import BaseModel

class InstrucaoCapacitacao(Base):
    '''Classe para estabelecer o modelo na tabela DB'''
    __tablename__ = "instrucaoCapacitacao"


    idCurso: int = Column("idCurso", ForeignKey("curso.id"), index=True)
    id: int = Column(Integer, primary_key = True, index = True)
    nome : str = Column(String(70), nullable = False)
    descricao : str = Column(String(800), nullable = False)
    dataCadastro : str= Column(String(20), nullable = False)


class InstrucaoCapacitacaoBase(BaseModel):
    idCurso: int
    nome: str
    descricao: str
    dataCadastro: str
    

class InstrucaoCapacitacaoRequest(InstrucaoCapacitacaoBase):
    '''...'''
    pass

class InstrucaoCapacitacaoRequestId(InstrucaoCapacitacaoBase):
    """Necessário para se fazer o update"""
    id : int

class InstrucaoCapacitacaoResponse(InstrucaoCapacitacaoBase):
    '''...'''
    id:int
    class Config:
        orm_mode = True

