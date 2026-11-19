from senha import senha_valida


def test_senha_com_exatamente_o_limite_e_aceita():
    senha = "Abcdef12"  # 8 caracteres
    resultado = senha_valida(senha)
    assert resultado is True


def test_senha_com_limite_menos_um_e_rejeitada():
    senha = "Abcdef1"  # 7 caracteres
    resultado = senha_valida(senha)
    assert resultado is False


def test_senha_vazia_e_rejeitada():
    senha = ""
    resultado = senha_valida(senha)
    assert resultado is False


def test_senha_so_com_espacos_e_rejeitada():
    senha = " " * 10  # 8 espacos mais 2, nada alem de espacos
    resultado = senha_valida(senha)
    assert resultado is False
