from pydantic import BaseModel
##from entities.Curso import Curso 
from src.domain.entities.Curso import Curso 
from enum import Enum
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Index
from sqlalchemy import Column, Enum 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ClassRoomBase(BaseModel):
    codigo:int 
    nome_turma: str
    data_inicio: str
    data_fim: str
    inicio_aula:str 
    fim_aula:str 
    capacidade_turma:int
    fk_curso:int
    professor:str 

# Pre requisito -> Crud prof 
##Classe turma sem atributos de curso e professor 
class ClassRoomDB(Base):
    __tablename__= "class"
    __table_args__ = {"extend_existing": True}


    codigo:int = Column(Integer(), primary_key= True , nullable= False)
    nome_turma: str = Column(String(70), nullable= False)
    data_inicio: str= Column(String(10), nullable= False)
    data_fim: str= Column(String(10), nullable= False)
    inicio_aula:str = Column(String(10), nullable=False)
    fim_aula:str = Column(String(10), nullable=False)
    capacidade_turma:int = Column(String(10), nullable=False)
    fk_curso:int = Column(Integer, ForeignKey(Curso.id))
    fk_professor:str = Column(String(), nullable=False)

class ClassRoomRequest(ClassRoomDB):
   '''...'''
   pass    

class ClassRoomResponse(ClassRoomDB):
    '''...'''
    class Config:
        orm_mode = True




     
