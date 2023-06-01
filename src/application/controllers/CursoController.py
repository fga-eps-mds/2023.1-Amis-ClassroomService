from database import get_db
from database import engine, Base
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, Response, status, HTTPException

from src.domain.entities.Curso import CursoResponse, CursoRequest
from infrastructure.repositories.CursoRepository import CursoRepository
from ...domain.repositories.CursoRepositoryBaseModel import CursoRepositoryBaseModel
from ...domain.entities.Curso import Curso, CursoBase
from ..useCases.CadastrarCursoUseCase import CursoUseCase
from application.controllers import  cursoUseCase

Base.metadata.create_all(bind=engine)


router_curso = APIRouter(
    prefix="/curso",
    tags=["curso"]
)



@router_curso.post("/", status_code=status.HTTP_201_CREATED,)
def create(curso_request: CursoRequest, database: Session = Depends(get_db)):

    curso_entitie = Curso(**curso_request.__dict__)

    cursoUseCase.save(cursoSent=curso_entitie)

    return curso_request

@router_curso.delete("/", status_code=status.HTTP_204_NO_CONTENT,)
def delete(curso_id: int):
    curso = cursoUseCase.find_by_id(curso_id)
    if curso is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

    cursoUseCase.delete_by_id(id=curso.id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_curso.get("/", response_model=list[CursoResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    curso = cursoUseCase.find_all()
    return curso

@router_curso.get("/{curso_id}",
                  response_model=CursoResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(curso_id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    curso = cursoUseCase.find_by_id(curso_id)

    if curso is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

    return curso
