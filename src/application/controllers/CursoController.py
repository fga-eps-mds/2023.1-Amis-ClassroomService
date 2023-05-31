from database import get_db
from database import engine, Base
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, Response
from src.domain.entities.Curso import CursoResponse, CursoRequest
from ...infrastructure.repositories.CursoRepository import CursoRepository
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

@router_curso.get("/", response_model=list[CursoBase])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    curso = cursoUseCase.find_all()
    return curso
