from sqlalchemy.orm import Session
from domain.entities.Register import Register
from typing import Callable, NoReturn
from domain.repositories import RegisterRepositoryBaseModel


class RegisterRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, registerSent: Register) -> Register:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(registerSent)
        session.commit()
        session.expunge_all()
        session.close()
        return registerSent
    
    def update(self, registerSent: Register) -> NoReturn:
        session = self.database()
        session.merge(registerSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Register]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        res = session.query(Register).all()
        session.close()
        return res

    def delete_by_id(self, register_id: int) -> NoReturn:
        """Função para deletar um register do DB, caso exista"""
        session = self.database()
        register_session = session.query(Register).filter(Register.idRegister == register_id).first()

        if register_session is not None:
            session.delete(register_session)
            session.commit()

        session.close()

    def find_by_id(self, register_id: int) -> Register | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Register).filter(Register.idRegister == register_id).first()


    """
    database: Callable[[], Session]

    def __init__(self, session:Callable[[],Session]):
        self.database = session 

    def save(self, registerSent: Register) -> Register:
        
        session=self.database ()
        api_client = AlunaApiClient()

        aluna_data = api_client.get_aluna(registerSent.idAluna)

        if aluna_data is not None:
            if registerSent.codigoTurma:
                registerSent.idAluna = int(id) 
                session.merge(registerSent)
                session.commit()
            else:
                session.add(registerSent)
                session.commit()
        else:
            raise Exception("Aluna id" + id + " não matriculada.")
        
        return registerSent
    """    

    # def find_all(self,database: Session) -> list[Register]:
    #     '''Função para fazer uma query de todas os register da DB'''
    #     return database.query(Register).all()

    # def find_by_id(self, id: str) -> Register:
    #     '''Função para fazer uma query por ID de um objeto Matricula na DB''' 
    #     session = self.database()
    #     return session.query(Register).filter(Register.codigoTurma == id).all()

    # def exists_by_id(self, codigoTurma: int, idAluna: int) -> bool:
    #     '''Função que verifica se a turma e aluna existe pelo ID dado na DB'''
    #     session = self.database()
    #     turma = session.query(Register).filter(Register.codigoTurma == codigoTurma, Register.idAluna == idAluna).first()
    #     print(turma)

    #     print(turma.idTurma, turma.idAluna)
    #     return turma is not None
    
    # def delete_by_id(self, codigoTurma: str, idAluna: str) -> None:
    #     '''Função para excluir uma aluna da turma no DB dado seu ID'''
    #     session = self.database()
    #     aluna = session.query(Register).filter(Register.idTurma == codigoTurma, Register.idAluna == idAluna).first()

    #     if aluna is not None:
    #         session.delete(aluna)
    #         session.commit()
    #         database.flush()