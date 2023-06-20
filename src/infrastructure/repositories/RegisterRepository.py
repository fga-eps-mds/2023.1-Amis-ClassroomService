from sqlalchemy.orm import Session
from domain.entities.Register import RegisterDB
from typing import Callable, NoReturn
from domain.repositories import RegisterRepositoryBaseModel


class RegisterRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, registerSent: RegisterDB) -> RegisterDB:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        print(f'estou no repositorio salvando o {registerSent.idAluna}')
        session.add(registerSent)
        session.commit()
        session.expunge_all()
        session.close()
        return registerSent
    
    def update(self, registerSent: RegisterDB) -> NoReturn:
        session = self.database()
        session.merge(registerSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[RegisterDB]:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        return session.query(RegisterDB).all()
        
    def find_all_student(self, codigoTurma: int ) -> RegisterDB | None:
        session = self.database()
        return session.query(RegisterDB.idAluna).filter_by(codigoTurma = codigoTurma).all()

    def delete_by_id(self, register_id: int) -> NoReturn:
        """Função para deletar um register do DB, caso exista"""
        session = self.database()
        register_session = session.query(RegisterDB).filter(RegisterDB.idRegister == register_id).first()

        if register_session is not None:
            session.delete(register_session)
            session.commit()

        session.close()

assert isinstance(RegisterRepository(
    {}), RegisterRepositoryBaseModel.RegisterRepositoryBaseModel)

