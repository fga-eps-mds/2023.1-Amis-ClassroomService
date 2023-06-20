'''Importando parâmetros da orm'''
from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base


class RegisterDB(Base):
    '''Classe para estabelecer o modelo na tabela DB'''
    __tablename__ = "register"
    __table_args__ = {"extend_existing": True}
    
    idAluna: int = Column(String(70), nullable= False)
    codigoTurma: int = Column("codigoTurma", ForeignKey("classRoom.codigo"), index=True)
    idRegister: int = Column(Integer, primary_key=True, index=True, nullable= False)
    

class RegisterBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    codigoTurma: int
    idAluna: int


class RegisterRequest(RegisterBase):
    '''...'''
    pass


class RegisterResponse(RegisterBase):
    '''...'''
    #idRegister:int
    class Config:
        orm_mode = True

class RegisterRequestId(RegisterBase):
    """Necessário para se fazer o update"""
    idRegister : int

class RegisterRequestCodigoTurma(RegisterBase):
    codigoTurma : int     