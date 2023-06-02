from domain.entities.Turma import ClassRoomDB
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable


##Protocolo das classes 
@runtime_checkable

class ClassRoomRepositoryBaseModel(Protocol):

    def save_class(self, database: Session, classSent: ClassRoomDB )-> ClassRoomDB:
        ...
        
    def find_all_class(self, database: Session)-> list[ClassRoomDB]:
        ...

    def delete_by_codigo(self, codigo: str)-> None:
        ...

    def update_class(self, database: Session, codigo: str, classSent: ClassRoomDB)-> ClassRoomDB:
        ...

    def find_by_codigo(self, database: Session, codigo: str)-> ClassRoomDB:
        ... 