from domain.entities.ClassRoom import ClassRoomDB, ClassRoomBase
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn


##Protocolo das classes 
@runtime_checkable

class ClassRoomRepositoryBaseModel(Protocol):

    def save_class(self, database: Session, class_sent: ClassRoomDB )-> ClassRoomDB:
        ...
        
    def find_all_class(self, database: Session)-> list[ClassRoomDB] | None:
        ...

    def find_classRoom_codigo(self, codigo: int) -> ClassRoomDB:
        ...

    def update_classRoom(self, class_sent = ClassRoomDB)-> NoReturn:
        ...

    def delete_classRoom_codigo(self, codigo:int)-> NoReturn:
        ...

    def validate_classRoom(self, class_room_base: ClassRoomBase)-> dict:
        ...

    
    
 