import random
from typing import List


def roll_dice(amount: int = 2) -> List[int]:
    """
    Simula o lançamento de dados.

    Args:
        amount (int): A quantidade de dados a serem lançados (padrão: 2).

    Returns:
        List[int]: Uma lista dos resultados dos lançamentos.
    """
    if amount <= 0:
        raise ValueError("A quantidade de dados deve ser maior que zero.")

    rolls: List[int] = []

    for _ in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    """
    Função principal que permite ao usuário rolar dados e encerrar o programa quando desejado.
    """
    while True:
        try:
            user_input: str = input("Insira a quantidade de dados que gostaria de rolar (ou 'sair' para encerrar): ")

            if user_input.lower() == "sair":
                print("Obrigado por jogar!")
                break

            num_rolls: int = int(user_input)
            results: List[int] = roll_dice(num_rolls)

            print(*results, sep=", ")

        except ValueError:
            print("Por favor, insira um valor válido.")


if __name__ == "__main__":
    main()
