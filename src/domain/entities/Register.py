'''Importando parâmetros da orm'''
from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base
from pydantic import BaseModel


class Register(Base):
    '''Classe para estabelecer o modelo na tabela DB'''
    __tablename__ = "register"
    __table_args__ = {"extend_existing": True}
    
    idRegister: int = Column(Integer, primary_key=True)
    # codigoTurma: int = Column("codigo", ForeignKey("classRoom.codigo"), index=True)
    codigoTurma: int = Column(Integer)
    idAluna: str = Column(String(70))
    #idAluna: int = Column("idAluna", ForeignKey("curso.id"), index=True)
    
    # classRoom = relationship("Classroom", backref="register")

class RegisterBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    codigoTurma: int
    idAluna: str

class RegisterRequest(RegisterBase):
    '''...'''
    pass


class RegisterResponse(RegisterBase):
    '''...'''
    idRegister: int
    class Config:
        orm_mode = True

class RegisterRequestId(RegisterBase):
    """Necessário para se fazer o update"""
    idRegister : int