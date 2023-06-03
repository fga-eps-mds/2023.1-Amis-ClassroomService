from database import get_db
from application.useCases.CadastrarCursoUseCase import CursoUseCase
from application.useCases.LoginClassRoom import ClassRoomUseCase 

from infrastructure.repositories.CursoRepository import CursoRepository
from infrastructure.repositories.ClassRoomRepository import ClassRoomRepository 
from database import SessionLocal

databaseSessionGenerator = SessionLocal


cursoRepository = CursoRepository(databaseSessionGenerator)
cursoUseCase = CursoUseCase(
    cursoRepository=cursoRepository
)

classRoomRepository = ClassRoomRepository(databaseSessionGenerator)
classUseCase = ClassRoomUseCase(
    classRoomRepository=classRoomRepository
)

