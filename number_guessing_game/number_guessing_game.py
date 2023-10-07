from random import randint


def guess_number(lower_number: int, higher_number: int) -> int:
    """
    Gera um número aleatório entre lower_number e higher_number e permite que o usuário adivinhe o número.

    Args:
        lower_number (int): O limite inferior do intervalo.
        higher_number (int): O limite superior do intervalo.

    Returns:
        int: O número adivinhado pelo usuário.
    """
    random_number: int = randint(lower_number, higher_number)

    print(f"Adivinhe um número entre {lower_number} até {higher_number}.")

    while True:
        try:
            user_guess: int = int(input("Adivinhe: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if user_guess > random_number:
            print(f"O número é menor que {user_guess}.")
        elif user_guess < random_number:
            print(f"O número é maior que {user_guess}.")
        else:
            print(f"Você acertou! O número é {random_number}.")
            return user_guess


if __name__ == "__main__":
    lower_limit: int = 1
    upper_limit: int = 10
    guessed_number: int = guess_number(lower_limit, upper_limit)
