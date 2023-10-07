def check_password(password: str) -> None:
    """
    Verifica se uma senha é comum ou única, comparando-a com uma lista de senhas comuns.

    Args:
        password (str): A senha a ser verificada.

    Returns:
        None
    """
    if not password:
        print("Senha vazia! Por favor, insira uma senha válida.")
        return

    with open("passwords.txt", "r") as file:
        commom_passwords: list[str] = file.read().splitlines()

    for i, commom_password in enumerate(commom_passwords, start=1):
        if password == commom_password:
            print(f"{password}: ❌ (#{i})")
            return

    print(f"{password}: ✅ (Senha Única)")


def main() -> None:
    """
    Função principal que solicita uma senha ao usuário e chama a função de verificação.
    """
    user_password: str = input("Insira uma senha: ")
    check_password(user_password)


if __name__ == '__main__':
    main()
