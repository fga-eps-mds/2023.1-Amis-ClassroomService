from application.useCases.RegisterUseCase import RegisterUseCase
from database import get_db
from application.useCases.CadastrarCursoUseCase import CursoUseCase
from application.useCases.LoginClassRoomUseCase import ClassRoomUseCase

from infrastructure.repositories.CursoRepository import CursoRepository
from infrastructure.repositories.RegisterRepository import RegisterRepository
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

registerRepository = RegisterRepository(databaseSessionGenerator)
registerUseCase = RegisterUseCase(
    registerRepository=registerRepository,
    classRoomRepository=classRoomRepository
)
