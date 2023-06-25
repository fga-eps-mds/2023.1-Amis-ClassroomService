from application.useCases.CadastrarCursoUseCase import CursoUseCase
from infrastructure.repositories.CursoRepository import CursoRepository
from domain.entities.Curso import Curso
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock


test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


curso_repo = CursoRepository(session=get_mock_db_session)
curso_use_case = CursoUseCase(
    cursoRepository=curso_repo,
)

test_list = [
    (Curso(
        id=1,
        nome="Curso de Confeitaria Avançada",
        descricao="Aprenda técnicas avançadas de confeitaria e crie sobremesas incríveis!",
        duracaoHoras=40,
    )),
    (Curso(
       id= 2,
        nome="Curso de Cozinha Italiana",
        descricao="Descubra os segredos da culinária italiana e prepare pratos autênticos.",
        duracaoHoras=60,
    )),
    (Curso(
        id=3,
        nome="Curso de Decoração de Bolos",
        descricao="Aprenda a decorar bolos de maneira criativa e impressione seus convidados.",
        duracaoHoras=30,
        )   ),
    (Curso(
        id=4,
        nome="Curso de Costura Criativa",
        descricao="Crie peças únicas e personalizadas utilizando técnicas de costura.",
        duracaoHoras=50,
    )),
    (Curso(
        id=5,
        nome="Curso de Patchwork",
        descricao="Aprenda a técnica do patchwork e crie belos trabalhos em tecido.",
        duracaoHoras=40,
    )),
]


@pytest.mark.parametrize(
    "curso_sent",
    test_list,
)
def test_save_curso_valido(curso_sent):
    """Testa se o curso é salvo com sucesso, assume que sempre recebe um curso válido"""
    print(curso_sent.__dict__)
    print(curso_use_case.find_all())
    response = curso_use_case.save(cursoSent=curso_sent)
    assert curso_sent == response, response.__dict__


def test_curso_find_all_ja_cadastrados():
    response = curso_use_case.find_all()
    response = [r.__dict__ for r in response]
    sorted(response, key=lambda x: x['id'])
    print(response)

    expected = [r.__dict__ for r in test_list]
    sorted(expected, key=lambda x: x['id'])
    print(expected)

    assert len(response) == len(test_list), response