from application.useCases.RegisterUseCase import RegisterUseCase
from infrastructure.repositories.RegisterRepository import RegisterRepository
from infrastructure.repositories.ClassRoomRepository import ClassRoomRepository
from domain.entities.Register import RegisterDB
from unittest.mock import MagicMock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
 
    return test_session


register_rep = RegisterRepository(session=get_mock_db_session)
classroom_rep = ClassRoomRepository(session=get_mock_db_session)
instrucao_use_case = RegisterUseCase(
    registerRepository=register_rep,
    classRoomRepository=classroom_rep,
)

test_list = [
    (RegisterDB(
        idAluna='pedrex.student',
        codigoTurma=1,
    )),
    (RegisterDB(
        idAluna='mario.student',
        codigoTurma=1,
    )),
]


@pytest.mark.parametrize(
    "register_sent",
    test_list,
)


def test_save_instrucao_valida(register_sent):
  
    response = instrucao_use_case.save(register_sent=register_sent)
    assert register_sent == response, response.__dict__