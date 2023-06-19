from typing import NoReturn
from domain.entities.Register import RegisterDB, RegisterBase, RegisterRequestId, RegisterResponse, RegisterRequest
from domain.repositories.RegisterRepositoryBaseModel import RegisterRepositoryBaseModel
from domain.repositories.ClassRoomRepositoryBaseModel import ClassRoomRepositoryBaseModel
from fastapi import HTTPException, status

#from infrastructure.repositories import RegisterRequest


class RegisterUseCase():

    __registerRepository__: RegisterRepositoryBaseModel
    __classRoomRepository__: ClassRoomRepositoryBaseModel

    def __init__(self, registerRepository: RegisterRepositoryBaseModel, 
                 classRoomRepository:ClassRoomRepositoryBaseModel
    ):
        self.__registerRepository__ = registerRepository
        self.__classRoomRepository__= classRoomRepository
    
    def find_by_id(self, codigoTurma : int) -> RegisterBase | None:
        return self.__registerRepository__.find_by_id(codigoTurma = codigoTurma)

    def delete_by_id(self, register_id: int) -> None:
        return self.__registerRepository__.delete_by_id(register_id=register_id)    
    
    def save(self, register_sent: RegisterDB) -> RegisterDB:
        
        # ids_aluna = register_sent.idAluna.split(',')
        # id_aluna_return = []
        # print(type(ids_aluna))
        # for id in ids_aluna:
        #     #id_register = id_register+1
        #     register_sent.idAluna = id
        #     print(f'atribuição {register_sent.idAluna}')
        #     #id_aluna_return.append(id)
        #     result = self.__registerRepository__.save(registerSent=register_sent)
        #     print(f'Os id:{id}')
        #     print(f'Resultado{result}')
        #     id_aluna_return.append(result)
        return self.__registerRepository__.save(registerSent=register_sent)
        
    def update(self, registerSent: RegisterRequestId) -> NoReturn:
        """Sobrescreve os dados de um register, assume que ele já exista"""
        self.__registerRepository__.update(RegisterDB(**registerSent.__dict__))


"""     def find_all(self, codigoTurma: int ) -> list[]:
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
"""
    







