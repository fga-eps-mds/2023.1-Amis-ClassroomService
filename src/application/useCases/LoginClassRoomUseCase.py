from domain.repositories.ClassRoomRepositoryBaseModel import ClassRoomRepositoryBaseModel
from domain.entities.ClassRoom import  ClassRoomRequestCodigo, ClassRoomDB, ClassRoomResponse, ClassRoomBase
from fastapi import HTTPException, status 

from infrastructure.repositories.field_repository import FieldValidation 

class ClassRoomUseCase():
    __classRoomRepository__: ClassRoomRepositoryBaseModel

    def __init__(self, classRoomRepository: ClassRoomRepositoryBaseModel):
        self.__classRoomRepository__ = classRoomRepository

    def save_class(self, classSent: ClassRoomDB) -> ClassRoomDB:
        return self.__classRoomRepository__.save_class(classSent=classSent)

    
    def find_all_class(self)-> list[ClassRoomResponse]:
        classRoom_db = self.__classRoomRepository__.find_all_class()
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
                fk_professor = classI_db.fk_professor,
                descricao = classI_db.descricao
            )
            classRomns.append(classRoom)
        return classRomns 

    def find_classRoom_codigo(self, codigo:int) ->ClassRoomBase | None:
        return self.__classRoomRepository__.find_classRoom_codigo(codigo=codigo)

    def update_classRoom(self, classSent:ClassRoomRequestCodigo):
        self.__classRoomRepository__.update_classRoom(ClassRoomDB(**classSent.__dict__))   
    
    def delete_classRoom_codigo(self, codigo:int) -> None:
        return self.__classRoomRepository__.delete_classRoom_codigo(codigo=codigo)

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

        completeStatus = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                completeStatus = False
                break
        fieldInfoDict['completeStatus'] = completeStatus    

        return fieldInfoDict

