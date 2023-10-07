import secrets
import string


def contains_upper(password: str) -> bool:
    """
    Verifica se uma senha contém pelo menos uma letra maiúscula.

    Args:
        password (str): A senha a ser verificada.

    Returns:
        bool: True se a senha contém pelo menos uma letra maiúscula, False caso contrário.
    """
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbols(password: str) -> bool:
    """
    Verifica se uma senha contém pelo menos um símbolo.

    Args:
        password (str): A senha a ser verificada.

    Returns:
        bool: True se a senha contém pelo menos um símbolo, False caso contrário.
    """
    for char in password:
        if char in string.punctuation:
            return True
    return False


def generate_password(length: int, symbols: bool = True, uppercase: bool = True) -> str:
    """
    Gera uma senha aleatória com opções para incluir símbolos e letras maiúsculas.

    Args:
        length (int): O comprimento da senha a ser gerada.
        symbols (bool): Se True, inclui símbolos na senha.
        uppercase (bool): Se True, inclui letras maiúsculas na senha.

    Returns:
        str: A senha gerada.
    """

    combination: str = string.ascii_lowercase

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    new_password: str = ""

    if symbols and uppercase:
        new_password += secrets.choice(string.punctuation)
        new_password += secrets.choice(string.ascii_uppercase)

    remaining_length = length - len(new_password)

    for _ in range(remaining_length):
        new_password += secrets.choice(combination)

    return new_password


if __name__ == '__main__':
    for i in range(1, 6):
        new_pass: str = generate_password(length=14, symbols=False, uppercase=False)
        specs: str = f"Letras Maiúsculas: {contains_upper(new_pass)}, Símbolos: {contains_symbols(new_pass)}"
        print(f"{i} -> {new_pass} ({specs})")
