from unittest import mock
from unittest.mock import MagicMock, patch
import pytest
from domain.entities.Register import RegisterDB, RegisterResponse, RegisterBase
from infrastructure.repositories.RegisterRepository import RegisterRepository
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

def generate_session():
    return MagicMock(spec=Session)

def test_save_new_student():
    # Arrange
    database = generate_session()
    test_session = database

    register = RegisterBase(
        idAluna= "mario.student",
        codigoTurma=1        
    )
    test_session.query().filter().first.return_value = None
    register_repository = RegisterRepository(database)

    # Act
    result = register_repository.save(register)

    # Assert"12234567890"
    assert result == register

    test_session.close()


def test_find_all():
    # Arrange
    database = generate_session()
    register_repository = RegisterRepository(database)
    expected_result = [RegisterDB(), RegisterDB()]
    database().query().all.return_value = expected_result

    # Act
    result = register_repository.find_all()

    # Assert
    assert result == expected_result

def test_find_all_student():
    # Arrange
    codigo_turma = 1
    database = generate_session()
    register_repository = RegisterRepository(database)
    expected_result = ["fagundes12", "lorraynecardozo", "mario.student"]  # Exemplo de lista de idAluna esperada

    # Criar uma lista de objetos RegisterDB com os valores de idAluna correspondentes
    register_objects = [RegisterDB(idAluna=x) for x in expected_result]
    
    # Configurar o retorno da chamada ao método all do objeto database().query()
    database().query().filter_by().all.return_value = register_objects

    # Act
    result = register_repository.find_all_student(codigo_turma)

    # Extrair os valores de idAluna da lista de objetos RegisterDB
    result_ids = [item.idAluna for item in result]
    print(result_ids)
    # Assert
    assert result_ids == expected_result