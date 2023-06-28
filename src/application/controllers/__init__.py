from database import get_db
from application.useCases.CadastrarCursoUseCase import CursoUseCase

from infrastructure.repositories.CursoRepository import CursoRepository

from database import SessionLocal

databaseSessionGenerator = SessionLocal


cursoRepository = CursoRepository(databaseSessionGenerator)
cursoUseCase = CursoUseCase(
    cursoRepository=cursoRepository
)
