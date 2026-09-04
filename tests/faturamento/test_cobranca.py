import pytest 
import time
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, valor_final",
    [
        #valor_base = 0, resultado -1
        (0, "BRONZE", 0, -1),
        #dias_atraso é negativo resultado -1
        (2, "BRONZE", -1, -1),
        #valor_base e dias_atraso é negativo resultado -2
        (0, "BRONZE", -2, -1),
        #plano bronze com outra sintaxe -2
        (100, "BR ONZ E", 1, -2),
        #plano prata com outra sintaxe
        (100, "pr A ta", 0, -2),
        #plano ouro com outra sintaxe
        (110, "oUr O", 0, -2),
        #plano vazio 
        (110, "", 0, -2),
        #plano platina invalido
        (102, "platina", 0, -2),
        (110, "BRONZE", 0, 110),
        (320, "OURO", 0, 240),
        (200, "PRATa", 0, 170),
        (1000, "ouro", 2, 764),

        (200, "PRATA", 3, 180.04),
        
        (378, "ouRO", 3, 294.9)
    ]
)
def test_final_cobranca(
    valor_base, plano, dias_atraso, valor_final
):
    assert processar_cobranca(valor_base, plano, dias_atraso) == valor_final

def test_velocidade_execucao():
    inicio = time.perf_counter()
    resultado = processar_cobranca(200, "prata", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado == 170
    assert tempo_decorrido < 0.8