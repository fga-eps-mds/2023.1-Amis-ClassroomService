'''Importando parâmetros da orm'''
from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RegisterDB(Base):
    '''Classe para estabelecer o modelo na tabela DB'''
    __tablename__ = "register"
    __table_args__ = {"extend_existing": True}
    
    idAluna: str = Column(String(70), nullable= False)
    codigoTurma: int  = Column(Integer, nullable= False)
    idRegister: int = Column(Integer, primary_key=True, nullable= False)
    
    # codigoTurma: int = Column("codigo", ForeignKey("classRoom.codigo"), index=True)
    #idAluna: int = Column("idAluna", ForeignKey("curso.id"), index=True)
    # classRoom = relationship("Classroom", backref="register")


class RegisterBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    codigoTurma: int
    idAluna: str
    idRegister : int

class RegisterRequest(RegisterBase):
    '''...'''
    pass


class RegisterResponse(RegisterBase):
    '''...'''
    class Config:
        orm_mode = True

class RegisterRequestId(RegisterBase):
    """Necessário para se fazer o update"""
    idRegister : int