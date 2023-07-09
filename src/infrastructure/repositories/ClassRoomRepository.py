from sqlalchemy.orm import Session
from domain.entities.ClassRoom import ClassRoomDB
from domain.repositories import ClassRoomRepositoryBaseModel
from infrastructure.repositories.field_repository import FieldValidation
from typing import Callable, NoReturn

class ClassRoomRepository:

    database: Callable[[],Session]
    def __init__(self,session:Callable[[],Session]):
        self.database = session 

    def save_class(self,class_sent: ClassRoomDB ) -> ClassRoomDB:
        session = self.database()

        session.add(class_sent)
        session.commit()
        session.expunge_all()
        session.close()
        return class_sent
    
    def find_all_class(self) -> list[ClassRoomDB]:
        session = self.database()
        res = session.query(ClassRoomDB).all()
        session.close()
        return res

    def find_class_room_codigo(self, codigo:int)-> ClassRoomDB | None:
        session = self.database()
        return session.query(ClassRoomDB).filter(ClassRoomDB.codigo == codigo).first()
                                               

    def update_class_room(self, class_sent: ClassRoomDB)-> NoReturn:
        session = self.database()
        session.merge(class_sent)
        session.commit()
        session.expunge_all()
        session.close()


    def delete_class_room_codigo(self, codigo:int)-> NoReturn:
        session = self.database()
        class_room_session = session.query(ClassRoomDB).filter(ClassRoomDB.codigo == codigo).first()

        if class_room_session is not None:
            session.delete(class_room_session)
            session.commit()
        session.close()
        
            

    def validate_class_room(self, classRoom: ClassRoomDB) -> dict:
        field_info_dict = {}
        field_info_dict["nomeTurma"] = vars(FieldValidation.nomeTurmaValidation(
            classRoom.nome_turma
        ))
        field_info_dict["dataInicio"] = vars(FieldValidation.data_inicio(
            classRoom.data_inicio
        ))
        field_info_dict["dataFim"] = vars(FieldValidation.data_fim(
            classRoom.data_fim
        ))
        field_info_dict["inicioAula"] = vars(FieldValidation.inicioAulaValidation(
            classRoom.inicio_aula
        ))
        field_info_dict["fimAula"] = vars(FieldValidation.fimAulaValidation(
            classRoom.fim_aula
        ))
        field_info_dict["Professor"] = vars(FieldValidation.professorValidation(
            classRoom.fk_professor
        ))
        
        complete_status = True
        for key in field_info_dict:
            if field_info_dict[key]['status'] == False:
                complete_status = False
                break
        field_info_dict['complete_status'] == complete_status    

        return field_info_dict
        
assert isinstance(ClassRoomRepository(
    {}), ClassRoomRepositoryBaseModel.ClassRoomRepositoryBaseModel)    

