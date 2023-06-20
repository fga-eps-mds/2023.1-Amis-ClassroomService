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
    
    def find_all(self) -> list[RegisterResponse]:
        register_db = self.__registerRepository__.find_all()
        registers = []
        for registerI in register_db:
            register = RegisterResponse(
                idAluna= registerI.idAluna,
                codigoTurma= registerI.codigoTurma,
                
            )
            registers.append(register)
        return registers    

    def find_all_student(self, codigoTurma:int)-> RegisterDB | None:
        return self.__registerRepository__.find_all_student(codigoTurma=codigoTurma)
    
    def delete_by_id(self, register_id: int) -> None:
        return self.__registerRepository__.delete_by_id(register_id=register_id)    
    
    def save(self, register_sent: RegisterDB) -> RegisterDB:
        return self.__registerRepository__.save(registerSent=register_sent)
        
    def update(self, registerSent: RegisterRequestId) -> NoReturn:
        """Sobrescreve os dados de um register, assume que ele já exista"""
        self.__registerRepository__.update(RegisterDB(**registerSent.__dict__))
