from database import get_db
from application.useCases.CadastrarCursoUseCase import CursoUseCase
from application.useCases.CadastrarInstrucaoCapacitacaoUseCase import InstrucaoCapacitacaoUseCase

from infrastructure.repositories.CursoRepository import CursoRepository
from infrastructure.repositories.InstrucaoCapacitacaoRepository import InstrucaoCapacitacaoRepository
from database import SessionLocal

databaseSessionGenerator = SessionLocal


cursoRepository = CursoRepository(databaseSessionGenerator)
cursoUseCase = CursoUseCase(
    cursoRepository=cursoRepository
)


instrucaoCapacitacaoRepository = InstrucaoCapacitacaoRepository(databaseSessionGenerator)
instrucaoCapacitacaoUseCase = InstrucaoCapacitacaoUseCase(
    instrucaoCapacitacaoRepository=instrucaoCapacitacaoRepository
)
