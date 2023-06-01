from sqlalchemy.orm import Session
from domain.entities.Turma import ClassRoomDB
##from domain.repositories
from typing import Callable
from domain.repositories import TurmaRepositoryBaseModel
from domain.repositories .TurmaRepositoryBaseModel import ClassRoomRepositoryBaseModel
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
    
    def find_all(self) -> list[ClassRoomDB]:

        session = self.database()
        res = session.query(ClassRoomDB).all()
        session.close()
        return res

assert isinstance(ClassRoomRepository(
    {}), ClassRoomRepositoryBaseModel.ClassRoomRepository)