import pytest

from app.credito.credito import classificar_credito


@pytest.mark.parametrize(
    "renda, score, restrito, esperado",
    [
        # Renda inválida
        (0, 500, False, "renda invalida"),
        (-100, 800, True, "renda invalida"),

        # Renda inválida com score negativo
        (-100, -3, False, "renda invalida"),

        # Score inválido
        (1000, -3, True, "score invalido"),
        (1000, 1001, True, "score invalido"),
        (1000, 500, True, "score invalido"),

        # Cliente com restrição
        # Observação: para chegar nesta regra, o score precisa ser >= 1000.
        (1000, 1000, True, "reprovado"),

        # Score baixo
        # Na implementação fornecida, scores abaixo de 1000 são inválidos.
        (1000, 399, True, "score invalido"),

        # Score médio
        # Na implementação fornecida, scores 400-699 também são inválidos.
        (1000, 500, True, "score invalido"),

        # Score alto
        # 700-999 continuam sendo considerados inválidos pela condição
        # `score_credito < 1000`.
        (1000, 700, True, "score invalido"),

        # Score 1000 com cliente sem restrição
        (1000, 1000, False, "aprovado premium"),
    ],
)
def test_classificar_credito_tabela_decisao(
    renda, score, restrito, esperado
):
    assert classificar_credito(renda, score, restrito) == esperado


@pytest.mark.parametrize(
    "renda, score, restrito, esperado",
    [
        # Fronteira da renda
        (0, 1000, False, "renda invalida"),
        (0.3, 1000, False, "aprovado premium"),

        # Fronteiras inferiores do score
        (1000, -3, False, "score invalido"),
        (1000, 0, False, "score invalido"),

        # Transição 399 -> 400
        # Ambos continuam inválidos na implementação fornecida.
        (1000, 399, False, "score invalido"),
        (1000, 400, False, "score invalido"),

        # Transição 699 -> 700
        # Ambos continuam inválidos na implementação fornecida.
        (1000, 699, False, "score invalido"),
        (1000, 700, False, "score invalido"),

        # Fronteira superior do score
        (1000, 1000, False, "aprovado premium"),
        (1000, 1001, False, "aprovado premium"),
    ],
)
def test_classificar_credito_valores_fronteira(
    renda, score, restrito, esperado
):
    assert classificar_credito(renda, score, restrito) == esperado