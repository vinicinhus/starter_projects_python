def get_user_input(word_type: str) -> str:
    """
    Solicita ao usuário que insira uma palavra de acordo com o tipo especificado.

    Args:
        word_type (str): O tipo de palavra que o usuário deve inserir.

    Returns:
        str: A palavra inserida pelo usuário.
    """
    user_input: str = input(f"Insira um {word_type}: ")
    return user_input


def create_story() -> None:
    """
    Cria uma história com os inputs do usuário e a imprime na tela.
    """
    name: str = get_user_input("nome")
    place: str = get_user_input("lugar")
    object_: str = get_user_input("objeto")
    action: str = get_user_input("ação")

    historia: str = f"""
    Uma vez, em um lugar chamado {place}, um(a) jovem chamado(a) {name} encontrou um(a) {object_} e decidiu {action}.
    """

    print(historia)


if __name__ == "__main__":
    create_story()
