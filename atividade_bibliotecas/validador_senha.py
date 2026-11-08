import re


def verificar_senha(senha):
    erros = []

    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")
    if not re.search(r"[A-Z]", senha):
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")
    if not re.search(r"[0-9]", senha):
        erros.append("A senha deve conter pelo menos um número.")

    return len(erros) == 0, erros
