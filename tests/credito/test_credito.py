import pytest
from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, resultado_esperado",
    [
        (0,123,True,"renda invalida"),
        (0,-1,True,"renda invalida"),
        (1,-5,False,"score invalido"),
        (18,1230,False,"score invalido"),
        (28,900,True,"reprovado"),
        (7,340,False,"reprovado"),
        (22,400,False,"aprovado padrao"),
        (19,700,False,"aprovado premium"),
    ]
)
def test_classificar_credito_caixa_preta(
    renda_mensal, score_credito, restrito, resultado_esperado
):
    assert classificar_credito (renda_mensal, score_credito, restrito) == resultado_esperado

#2
@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, resultado_esperado",
    [
        (0,123,True,"renda invalida"),
        (0.01,0,True,"reprovado"),
        (32,-5,False,"score invalido"),
        (18,0,False,"reprovado"),
        (67,399,False,"reprovado"),
        (7,400,False,"aprovado padrao"),
        (22,699,False,"aprovado padrao"),
        (19,700,False,"aprovado premium"),
        (19,1000,False,"aprovado premium"),
        (19,1001,False,"score invalido"),
    ]
)
def test_classificar_credito_caixa_preta_transicao(
    renda_mensal, score_credito, restrito, resultado_esperado
):
    assert classificar_credito (renda_mensal, score_credito, restrito) == resultado_esperado
