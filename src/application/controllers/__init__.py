from database import get_db
from application.useCases.CadastrarCursoUseCase import CursoUseCase
from application.useCases.LoginClassRoomUseCase import ClassRoomUseCase 

from infrastructure.repositories.CursoRepository import CursoRepository
from infrastructure.repositories.ClassRoomRepository import ClassRoomRepository 
from database import SessionLocal
from infrastructure.repositories.InstrucaoCapacitacaoRepository import InstrucaoCapacitacaoRepository
from application.useCases.CadastrarInstrucaoCapacitacaoUseCase import InstrucaoCapacitacaoUseCase

databaseSessionGenerator = SessionLocal


cursoRepository = CursoRepository(databaseSessionGenerator)
cursoUseCase = CursoUseCase(
    cursoRepository=cursoRepository
)

classRoomRepository = ClassRoomRepository(databaseSessionGenerator)
classUseCase = ClassRoomUseCase(
    classRoomRepository=classRoomRepository
)


instrucaoCapacitacaoRepository = InstrucaoCapacitacaoRepository(databaseSessionGenerator)
instrucaoCapacitacaoUseCase = InstrucaoCapacitacaoUseCase(
    instrucaoCapacitacaoRepository=instrucaoCapacitacaoRepository
)

