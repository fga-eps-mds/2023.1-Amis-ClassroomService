from typing import NoReturn
from domain.entities.Register import Register, RegisterBase, RegisterRequestId, RegisterResponse, RegisterRequest
from domain.repositories.RegisterRepositoryBaseModel import RegisterRepositoryBaseModel
from domain.repositories.ClassRoomRepositoryBaseModel import ClassRoomRepositoryBaseModel
from fastapi import HTTPException, status

#from infrastructure.repositories import RegisterRequest


class RegisterUseCase():

    __registerRepository__: RegisterRepositoryBaseModel
    __classRoomRepository__: ClassRoomRepositoryBaseModel

    def __init__(
        self,
        registerRepository: RegisterRepositoryBaseModel,
        classRoomRepository:ClassRoomRepositoryBaseModel
    ):
        self.__registerRepository__ = registerRepository,
        self.__classRoomRepository__= classRoomRepository

    #def save(self, registerSent: list[Register]) -> list[Register]:
    def save(self, registerSent: Register) -> Register:
        '''Função para salvar um objeto SocialWorker na DB, utilizada também como update'''
        """
        try:
            new_registers=[]
            for req in registerSent:
                self.__registerRepository__.save(registerSent=req)
        except Exception as error:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(error))
        '''Função para salvar um objeto Register na DB, utilizada também como update'''
        return new_registers
        """
        return self.__registerRepository__.save(registerSent=registerSent)
    


    def delete_by_id(self, id: int) -> None:
        return self.__registerRepository__.delete_by_id(id)


    def find_all(self) -> list[RegisterResponse]:
        registers_db = self.__registerRepository__.find_all()
        registers = []
        for register_db in registers_db:
            register = RegisterResponse(
                codigoTurma=register_db.codigoTurma,
                idAluna=register_db.idAluna,
                idRegister=register_db.idRegister
            )
            registers.append(register)
        return registers
    
    def find_by_id(self, register_id : int) -> RegisterBase | None:
        return self.__registerRepository__.find_by_id(register_id=register_id)
    

    def find_by_id_turma(self, codigoTurma : int) -> RegisterBase | None:
        return self.__classRoomRepository__.find_classRoom_codigo(codigo=codigoTurma)
    
    
    def update(self, registerSent: RegisterRequestId) -> NoReturn:
        """Sobrescreve os dados de um register, assume que ele já exista"""
        self.__registerRepository__.update(Register(**registerSent.__dict__))

    # def update(self, registerSent: RegisterRequestId) -> NoReturn:
    #     """Sobrescreve os dados de um register, assume que ele já exista"""
    #     self.__registerRepository__.update(register(**registerSent.__dict__))


    """
    __registerRepository__: RegisterRepositoryBaseModel

    def __init__(
        self,
        registerRepository: RegisterRepositoryBaseModel
    ):
        self.__registerRepository__ = registerRepository

    def save(self, registerSent: list[RegisterRequest]) -> list[RegisterRequest]:
        try:
            new_registers = []
            for req in registerSent:
                new_register = self.__registerRepository__.save(req)
                new_registers.append(new_register)
        except Exception as error:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(error))
        '''Função para salvar um objeto Register na DB, utilizada também como update'''
        return new_registers
  """  
    # def find_all(self) -> list[RegisterResponse]:
    #     register_db = self.__registerRepository__.find_all()
    #     registers = []
    #     for register_db in register_db:
    #         register = RegisterResponse(
    #             id=register_db.id,
    #             nome=register_db.nome,
    #             descricao=register_db.descricao,
    #             duracaoHoras=register_db.duracaoHoras
    #         )
    #         register.append(register)
    #     return register