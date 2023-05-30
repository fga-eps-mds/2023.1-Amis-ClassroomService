from database import get_db
from database import engine, Base
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends, Response
from src.domain.entities.Curso import CursoResponse, CursoRequest
from ...infrastructure.repositories.CursoRepository import CursoRepository
from ...domain.entities.Curso import Curso
from ..useCases.CadastrarCursoUseCase import CursoService
from application.controllers import  cursoService

Base.metadata.create_all(bind=engine)


router_curso = APIRouter(
    prefix="/curso",
    tags=["curso"]
)



@router_curso.post("/", status_code=status.HTTP_201_CREATED,)
def create(curso_request: CursoRequest, database: Session = Depends(get_db)):

    curso_entitie = Curso(**curso_request.__dict__)

    cursoService.save(cursoSent=curso_entitie)

    return curso_request