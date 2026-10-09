def calcular_desconto_combo(quantidade_itens: int, tipo_cliente: str) -> float:
    """
    Calcula o desconto aplicado a um combo com base na quantidade de itens e no tipo de cliente.
    """
    desconto = 0.0

    if quantidade_itens < 2:
        return 0.0

    perfil = tipo_cliente.strip().lower() if tipo_cliente else ""

    if perfil == "estudante":
        if quantidade_itens >= 5:
            return 0.20
        return 0.15
    
    if perfil == "professor":
        return 0.10
        
    return 0.10