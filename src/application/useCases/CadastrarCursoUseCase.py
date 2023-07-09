from domain.entities.Curso import Curso, CursoResponse, CursoBase, CursoRequestId
from domain.repositories.CursoRepositoryBaseModel import CursoRepositoryBaseModel
from typing import NoReturn

class CursoUseCase():
    __curso_repository__: CursoRepositoryBaseModel

    def __init__(
        self,
        curso_repository: CursoRepositoryBaseModel
    ):
        self.__cursoRepository__ = curso_repository

    def save(self, curso_sent: Curso) -> Curso:
        '''Função para salvar um objeto SocialWorker na DB, utilizada também como update'''
        return self.__cursoRepository__.save(cursoSent=curso_sent)

    def delete_by_id(self, id: int) -> None:
        return self.__cursoRepository__.delete_by_id(curso_id=id)


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

    def find_by_id(self, curso_id : int) -> CursoBase | None:
        return self.__cursoRepository__.find_by_id(curso_id=curso_id)

    def update(self, curso_sent: CursoRequestId) -> NoReturn:
        """Sobrescreve os dados de um curso, assume que ele já exista"""
        self.__cursoRepository__.update(Curso(**curso_sent.__dict__))
