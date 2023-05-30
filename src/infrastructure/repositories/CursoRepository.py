from sqlalchemy.orm import Session
from ...domain.entities import Curso


class CursoRepository:

    @staticmethod
    def save_curso(db: Session, curso: Curso) -> Curso:
        if curso.id_curso:
            db.merge(curso)
        else:
            db.add(curso)
        db.commit()
        return curso