from pydantic import BaseModel
##from entities.Curso import Curso 
from src.domain.entities.Curso import Curso 
from enum import Enum
from database import Base, SessionLocal, engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Index
from sqlalchemy import Column, Enum 
from sqlalchemy.ext.declarative import declarative_base


class ClassRoomDB(Base):
    __tablename__= "classRoom"
    #__table_args__ = {"extend_existing": True}
        
    codigo: int = Column(Integer, primary_key= True , nullable= False, index=True)
    nome_turma: str = Column(String(70), nullable= False)
    data_inicio: str= Column(String(10), nullable= False)
    data_fim: str= Column(String(10), nullable= False)
    inicio_aula: str = Column(String(10), nullable=False)
    fim_aula: str = Column(String(10), nullable=False)
    capacidade_turma: int = Column(Integer, nullable=False)
    fk_curso: int = Column(Integer, nullable=False,)
    fk_professor: str = Column(String(100), nullable=False)
    descricao: str = Column(String(500), nullable=True)
    

class ClassRoomBase(BaseModel):
    nome_turma: str
    data_inicio: str
    data_fim: str
    inicio_aula:str 
    fim_aula:str 
    capacidade_turma:int
    fk_curso:int
    fk_professor:str
    descricao:str

# Pre requisito -> Crud prof 
##Classe turma sem atributos de curso e professor 


class ClassRoomRequest(ClassRoomBase):
   '''...'''
   pass

class ClassRoomResponse(ClassRoomBase):
    '''...'''
    codigo:int  # tirar se for pra inserir
    class Config:
        orm_mode = True

class ClassRoomRequestCodigo(ClassRoomBase):
    codigo: int 



     
