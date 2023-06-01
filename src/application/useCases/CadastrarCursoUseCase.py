from domain.entities.Curso import Curso, CursoResponse
from domain.repositories.CursoRepositoryBaseModel import CursoRepositoryBaseModel
from fastapi import HTTPException, status

class CursoUseCase():
    __cursoRepository__: CursoRepositoryBaseModel

    def __init__(
        self,
        cursoRepository: CursoRepositoryBaseModel
    ):
        self.__cursoRepository__ = cursoRepository

    def save(self, cursoSent: Curso) -> Curso:
        '''Função para salvar um objeto SocialWorker na DB, utilizada também como update'''
        return self.__cursoRepository__.save(cursoSent=cursoSent)

    def delete(self, cursoSent: Curso) -> None:
        return self.__cursoRepository__.delete_by_id(cursoSent=cursoSent)


    def find_all(self) -> list[CursoResponse]:
        cursos_db = self.__cursoRepository__.find_all()
        cursos = []
        for curso_db in cursos_db:
            curso = CursoResponse(
                id=curso_db.id,
                nome=curso_db.nome,
                descricao=curso_db.descricao,
                duracaoHoras=curso_db.duracaoHoras
            )
            cursos.append(curso)
        return cursos
