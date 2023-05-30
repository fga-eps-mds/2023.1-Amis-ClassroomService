from domain.entities.Curso import Curso, CursoBase, CursoRequest, CursoResponse
from domain.repositories.CursoRepositoryBaseModel import CursoRepositoryBaseModel
from fastapi import HTTPException, status

class CursoService():
    __cursoRepository__: CursoRepositoryBaseModel

    def __init__(
        self,
        cursoRepository: CursoRepositoryBaseModel
    ):
        self.__cursoRepository__ = cursoRepository

    def save(self, cursoSent: Curso) -> Curso:
        '''Função para salvar um objeto SocialWorker na DB, utilizada também como update'''
        return self.__cursoRepository__.save(cursoSent=cursoSent)