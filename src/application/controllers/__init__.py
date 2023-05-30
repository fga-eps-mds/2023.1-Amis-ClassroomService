from database import get_db
from application.useCases.CadastrarCursoUseCase import CursoService

from infrastructure.repositories.CursoRepository import CursoRepository
from database import SessionLocal

databaseSessionGenerator = SessionLocal


cursoRepository = CursoRepository(databaseSessionGenerator)
cursoService = CursoService(
    cursoRepository=cursoRepository
)
