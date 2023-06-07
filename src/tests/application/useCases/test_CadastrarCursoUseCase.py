from application.useCases.CadastrarCursoUseCase import CursoUseCase
from infrastructure.repositories.CursoRepository import CursoRepository
from domain.entities.Curso import Curso
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
import pytest


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return MagicMock(spec=Session)


curso_repo = CursoRepository(session=get_mock_db_session)
curso_use_case = CursoUseCase(
    cursoRepository=curso_repo,
)


@pytest.mark.parametrize(
    "id, nome, descricao, duracaoHoras",
    [
        (
            1,
            "Curso de Confeitaria Avançada",
            "Aprenda técnicas avançadas de confeitaria e crie sobremesas incríveis!",
            40,
        ),
        (
            2,
            "Curso de Cozinha Italiana",
            "Descubra os segredos da culinária italiana e prepare pratos autênticos.",
            60,
        ),
        (
            3,
            "Curso de Decoração de Bolos",
            "Aprenda a decorar bolos de maneira criativa e impressione seus convidados.",
            30,
        ),
        (
            4,
            "Curso de Costura Criativa",
            "Crie peças únicas e personalizadas utilizando técnicas de costura.",
            50,
        ),
        (
            5,
            "Curso de Patchwork",
            "Aprenda a técnica do patchwork e crie belos trabalhos em tecido.",
            40,
        ),
    ],
)
def test_save_curso_valido(id: int, nome: str, descricao: str, duracaoHoras: int):
    """Testa se o curso é salvo com sucesso, assume que sempre recebe um curso válido"""
    curso_sent = Curso(
        id=42,
        nome="Curso Teste !",
        descricao="Curso para fins de teste !",
        duracaoHoras=1,
    )
    response = curso_use_case.save(cursoSent=curso_sent)
    assert curso_sent == response, response.__dict__
