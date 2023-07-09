
from application.useCases.CadastrarInstrucaoCapacitacaoUseCase import InstrucaoCapacitacaoUseCase
from infrastructure.repositories.InstrucaoCapacitacaoRepository import InstrucaoCapacitacaoRepository

from domain.entities.InstrucaoCapacitacao import InstrucaoCapacitacao, InstrucaoCapacitacaoBase
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock


test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


instrucao_rep = InstrucaoCapacitacaoRepository(session=get_mock_db_session)
instrucao_use_case = InstrucaoCapacitacaoUseCase(
    instrucaoCapacitacaoRepository=instrucao_rep,
)

test_list = [
    (InstrucaoCapacitacao(
        id=500,
        nome="Instruções de patchwork",
        descricao="Aprenda a técnica do patchwork e crie belos trabalhos em tecido.",
        dataCadastro="2022-01-01",
        idCurso= 36,
    )),
    (InstrucaoCapacitacao(
        id=501,
        nome="Receita de Bolo",
        descricao="2 xícaras de massa e açúcar",
        dataCadastro="2022-01-01",
        idCurso= 36,
    )),
]


@pytest.mark.parametrize(
    "instrucaoCapacitacaoSent",
    test_list,
)


def test_save_instrucao_valida(instrucaoCapacitacaoSent):
    """Testa se o curso é salvo com sucesso, assume que sempre recebe um curso válido"""
    #print(instrucaoCapacitacaoSent.__dict__)
    #print(instrucao_use_case.find_all())
    response = instrucao_use_case.save(instrucaoCapacitacaoSent=instrucaoCapacitacaoSent)
    assert instrucaoCapacitacaoSent == response, response.__dict__


def test_instrucao_find_all_ja_cadastrados():
    response = instrucao_use_case.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['id'])
    print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['id'])
    print(sorted_expected)

    assert len(response) == len(test_list), response



def test_update_instrucao_valida():
    instrucao_existente = InstrucaoCapacitacao(
        id=500,
        nome="Curso de Patchwork",
        descricao="Aprenda a técnica do patchwork e crie belos trabalhos em tecido.",
        dataCadastro="2022-01-01",
        idCurso=36,
    )
    instrucao_use_case.save(instrucaoCapacitacaoSent=instrucao_existente)

    instrucao_atualizada = InstrucaoCapacitacao(
        id=500,
        nome="Curso de Patchwork",
        descricao="Aprenda a técnica do patchwork.",
        dataCadastro="2022-01-01",
        idCurso=36,
    )

    response = instrucao_use_case.update(instrucaoCapacitacaoSent=instrucao_atualizada)
    # Verificação se a resposta da instrução de capacitação foi atualizada corretamente
    assert instrucao_atualizada == response

