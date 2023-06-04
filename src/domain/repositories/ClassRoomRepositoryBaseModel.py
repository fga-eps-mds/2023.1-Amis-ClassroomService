from domain.entities.ClassRoom import ClassRoomDB, ClassRoomBase
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable


##Protocolo das classes 
@runtime_checkable

class ClassRoomRepositoryBaseModel(Protocol):

    def save_class(self, database: Session, classSent: ClassRoomDB )-> ClassRoomDB:
        ...
        
    def find_all_class(self, database: Session)-> list[ClassRoomDB]:
        ...

    
    def validate_classRoom(self, classRoomBase: ClassRoomBase)-> dict:
        ...

    
 