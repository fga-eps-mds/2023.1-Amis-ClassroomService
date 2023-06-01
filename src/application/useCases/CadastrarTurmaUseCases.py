from domain.repositories.TurmaRepositoryBaseModel import ClassRoomRepositoryBaseModel
from domain.entities.Turma import ClassRoomDB, ClassRoomResponse
from fastapi import HTTPException, status 

class ClassUseCase():
    __TurmaRepository__: ClassRoomRepositoryBaseModel

    def __init__(self, classRepository: ClassRoomRepositoryBaseModel):
        self.__TurmaRepository__ = classRepository

    def save_class(self, classSent: ClassRoomDB) -> ClassRoomDB:

        return self.__TurmaRepository__.save_class(classSent=classSent)

    
    def find_all_class(self)-> list[ClassRoomResponse]:
        classRoom_db = self.__TurmaRepository__.find_all_class()
        classRomns = []
        for classI_db in classRoom_db:
            classRoom = ClassRoomResponse(
                codigo = classI_db.codigo,
                nome_turma = classI_db.nome_turma,
                data_inicio = classI_db.data_inicio,
                data_fim = classI_db.data_fim,
                inicio_aula = classI_db.inicio_aula,
                fim_aula = classI_db.fim_aula, 
                capacidade_turma= classI_db.capacidade_turma,
                fk_curso = classI_db.fk_curso,
                professor = classI_db.professor
            )
            classRomns.append(classRoom)
        return classRomns    
            







