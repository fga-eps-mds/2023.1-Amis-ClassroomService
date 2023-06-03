from sqlalchemy.orm import Session
from domain.entities.ClassRoom import ClassRoomDB
from domain.repositories import ClassRoomRepositoryBaseModel
from infrastructure.repositories.field_repository import FieldValidation
from typing import Callable

class ClassRoomRepository:

    database: Callable[[],Session]
    def __init__(self,session:Callable[[],Session]):
        self.database = session 

    def save_class(self,classSent: ClassRoomDB ) -> ClassRoomDB:
        session = self.database()

        session.add(classSent)
        session.commit()
        session.expunge_all()
        session.close()
        return classSent
    
    def find_all_class(self) -> list[ClassRoomDB]:

        session = self.database()
        res = session.query(ClassRoomDB).all()
        session.close()
        return res

    def validate_classRoom(self, classRoom: ClassRoomDB) -> dict:
        fieldInfoDict = {}
        fieldInfoDict["nomeTurma"] = vars(FieldValidation.nomeTurmaValidation(
            classRoom.nome_turma
        ))
        fieldInfoDict["dataInicio"] = vars(FieldValidation.data_inicio(
            classRoom.data_inicio
        ))
        fieldInfoDict["dataFim"] = vars(FieldValidation.data_fim(
            classRoom.data_fim
        ))
        fieldInfoDict["inicioAula"] = vars(FieldValidation.inicioAulaValidation(
            classRoom.inicio_aula
        ))
        fieldInfoDict["fimAula"] = vars(FieldValidation.fimAulaValidation(
            classRoom.fim_aula
        ))
        fieldInfoDict["Professor"] = vars(FieldValidation.professorValidation(
            classRoom.fk_professor
        ))
        

assert isinstance(ClassRoomRepository(
    {}), ClassRoomRepositoryBaseModel.ClassRoomRepositoryBaseModel)    

