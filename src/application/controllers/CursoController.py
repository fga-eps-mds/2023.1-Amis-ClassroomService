from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from domain.entities.Curso import (CursoResponse,
                                   CursoRequest,
                                   Curso,
                                   CursoRequestId)
from application.controllers import  cursoUseCase

Base.metadata.create_all(bind=engine)


router_curso = APIRouter(
    prefix="/curso",
    tags=["curso"]
)



@router_curso.post("/", status_code=status.HTTP_201_CREATED)
def create(curso_request: CursoRequest):

    curso_entitie = Curso(**curso_request.__dict__)

    cursoUseCase.save(cursoSent=curso_entitie)

    return curso_request

@router_curso.put("/{id}", status_code=status.HTTP_201_CREATED)
def update(cursoSent: CursoRequestId):
    if cursoUseCase.find_by_id(cursoSent.id) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Curso não existente")
    cursoUseCase.update(cursoSent)


@router_curso.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
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

@router_curso.get("/{id}",
                  response_model=CursoResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(curso_id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    curso = cursoUseCase.find_by_id(curso_id)

    if curso is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

    return curso
