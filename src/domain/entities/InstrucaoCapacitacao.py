"""Importando parâmetros da orm"""
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from pydantic import BaseModel, Field

NOME_MAX = 70
DESCRICAO_MAX = 800
DATA_CADASTRO_MAX = 20


class InstrucaoCapacitacao(Base):
    """Classe para estabelecer o modelo na tabela DB"""

    __tablename__ = "instrucaoCapacitacao"

    idCurso: int = Column("idCurso", ForeignKey("curso.id"), index=True)
    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(NOME_MAX), nullable=False)
    descricao: str = Column(String(DESCRICAO_MAX), nullable=False)
    dataCadastro: str = Column(String(DATA_CADASTRO_MAX), nullable=False)


class InstrucaoCapacitacaoBase(BaseModel):
    idCurso: int = Field(descricao="Id do curso vinculado a instrução")
    nome: str = Field(descricao="Nome da capacitação", max_length=NOME_MAX)
    descricao: str = Field(
        descricao="Descrição da capacitação", max_length=DESCRICAO_MAX
    )
    dataCadastro: str = Field(
        descricao="Data de cadastro da capacitação", max_length=DATA_CADASTRO_MAX
    )


class InstrucaoCapacitacaoRequest(InstrucaoCapacitacaoBase):
    """..."""
    #id: int
    pass


class InstrucaoCapacitacaoRequestId(InstrucaoCapacitacaoBase):
    """Necessário para se fazer o update"""

    id: int


class InstrucaoCapacitacaoResponse(InstrucaoCapacitacaoBase):
    """..."""
    id: int

    class Config:
        orm_mode = True
