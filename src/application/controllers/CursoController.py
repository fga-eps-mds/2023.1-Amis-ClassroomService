from database import get_db
from database import engine, Base
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends
from src.domain.entities.Curso import CursoResponse, CursoRequest
from ...infrastructure.repositories.CursoRepository import CursoRepository
from ...domain.entities.Curso import Curso

Base.metadata.create_all(bind=engine)


router_curso = APIRouter(
    prefix="/curso",
    tags=["curso"]
)

@router_curso.post("/", response_model = CursoResponse, status_code=status.HTTP_201_CREATED)
def create_curso(request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.save_curso(db, Curso(**request.dict()))
    return CursoResponse.from_orm(curso)