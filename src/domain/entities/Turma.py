from pydantic import BaseModel
from enum import Enum
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Index
from sqlalchemy import Column, Enum 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ClassRoomBase(BaseModel):
    codigo:int 
    dataInicio: str
    data_fim: str
    horario_inicio:str 
    horario_inicio:str 
    capacidade_turma:int 

# Pre requisito -> Crud prof 
##Classe turma sem atributos de curso e professor 
class ClassRoomDB(Base):
    __tablename__= "class"
    __table_args__ = {"extend_existing": True}

    codigo:int = Column(Integer(70), primary_key= True , nullable= False)
    dataInicio: str= Column(String(10), nullable= False)
    data_fim: str= Column(String(10), nullable= False)
    horario_inicio:str = Column(String(10), nullable=False)
    horario_inicio:str = Column(String(10), nullable=False)
    capacidade_turma:int = Column(String(10), nullable=False)


class ClassRoomRequest(ClassRoomDB):
   '''...'''
   pass    

class ClassRoomResponse(ClassRoomDB):
    '''...'''
    class Config:
        orm_mode = True




     
