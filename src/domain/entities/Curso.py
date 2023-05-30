'''Importando parâmetros da orm'''
from sqlalchemy import Column, Integer, String
from database.py import Base



class Cursos(Base):
    '''Classe para estabelecer o modelo na tabela DB'''
    __tablename__ = "cursos"

    id = int = Column(Integer, primary_key = True, index = True)
    nome = str = Column(String(70), nullable = False)
    descricao = Column(String(300), nullable = False)
    duracaoHoras = Column(Integer, nullable = False)