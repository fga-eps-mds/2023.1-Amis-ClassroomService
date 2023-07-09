from domain.repositories.ClassRoomRepositoryBaseModel import ClassRoomRepositoryBaseModel
from domain.entities.ClassRoom import  ClassRoomRequestCodigo, ClassRoomDB, ClassRoomResponse, ClassRoomBase
from fastapi import HTTPException, status 

from infrastructure.repositories.field_repository import FieldValidation 

class ClassRoomUseCase():
    __class_room_repository__: ClassRoomRepositoryBaseModel

    def __init__(self, class_room_repository: ClassRoomRepositoryBaseModel):
        self.__classRoomRepository__ = class_room_repository

    def save_class(self, class_sent: ClassRoomDB) -> ClassRoomDB:
        return self.__classRoomRepository__.save_class(class_sent=class_sent)

    
    def find_all_class(self)-> list[ClassRoomResponse]:
        class_room_db = self.__classRoomRepository__.find_all_class()
        class_romns = []
        for class_i_db in class_room_db:
            classRoom = ClassRoomResponse(
 16-Arrumando-CodeSmells
                codigo = class_i_db.codigo,
                nome_turma = class_i_db.nome_turma,
                data_inicio = class_i_db.data_inicio,
                data_fim = class_i_db.data_fim,
                inicio_aula = class_i_db.inicio_aula,
                fim_aula = class_i_db.fim_aula, 
                capacidade_turma= class_i_db.capacidade_turma,
                fk_curso = class_i_db.fk_curso,
                fk_professor = class_i_db.fk_professor,
                descricao = class_i_db.descricao

                codigo = classI_db.codigo,
                nome_turma = classI_db.nome_turma,
                data_inicio = classI_db.data_inicio,
                data_fim = classI_db.data_fim,
                inicio_aula = classI_db.inicio_aula,
                fim_aula = classI_db.fim_aula, 
                capacidade_turma= classI_db.capacidade_turma,
                fk_curso = classI_db.fk_curso,
                fk_professor = classI_db.fk_professor,
                descricao= classI_db.descricao 
            )
            class_romns.append(classRoom)
        return class_romns 

    def find_class_room_codigo(self, codigo:int) ->ClassRoomBase | None:
        return self.__classRoomRepository__.find_classRoom_codigo(codigo=codigo)

    def update_class_room(self, class_sent:ClassRoomRequestCodigo):
        self.__classRoomRepository__.update_classRoom(ClassRoomDB(**class_sent.__dict__))   
    
    def delete_class_room_codigo(self, codigo:int) -> None:
        return self.__classRoomRepository__.delete_classRoom_codigo(codigo=codigo)

    def validate_class_room(self, class_room: ClassRoomDB) -> dict:
        fieldInfoDict = {}
        fieldInfoDict["nomeTurma"] = vars(FieldValidation.nomeTurmaValidation(
            class_room.nome_turma
        ))
        fieldInfoDict["dataInicio"] = vars(FieldValidation.data_inicio(
            class_room.data_inicio
        ))
        fieldInfoDict["dataFim"] = vars(FieldValidation.data_fim(
            class_room.data_fim
        ))
        fieldInfoDict["inicioAula"] = vars(FieldValidation.inicioAulaValidation(
            class_room.inicio_aula
        ))
        fieldInfoDict["fimAula"] = vars(FieldValidation.fimAulaValidation(
            class_room.fim_aula
        ))
        fieldInfoDict["Professor"] = vars(FieldValidation.professorValidation(
            class_room.fk_professor
        ))

        complete_status = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                complete_status = False
                break
        fieldInfoDict['complete_status'] = complete_status    

        return fieldInfoDict

