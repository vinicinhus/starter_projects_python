from random import choice


def run_game():
    """
    Executa o jogo da forca onde o jogador tenta adivinhar uma palavra escolhida aleatoriamente.
    """
    words: str = choice(
        ["abacaxi", "banana", "morango", "historia", "matematica", "geografia", "computador", "teclado", "monitor"])

    username: str = input("Qual é o seu nome? >> ")
    print(f"Bem-vindo ao jogo da forca, {username}!")

    guessed: str = ""
    tries: int = 5

    while tries > 0:
        blanks: int = 0

        print("Palavra: ", end="")

        for char in words:
            if char in guessed:
                print(char, end="")
            else:
                print("_", end="")
                blanks += 1

        print("\n")  # Adiciona um espaço em branco

        if blanks == 0:
            print("Você acertou!")
            break

        guess: str = input("Insira uma letra ou a palavra completa: ")

        if len(guess) == 1:
            if guess in guessed:
                print(f"Você já usou: '{guess}'. Por favor, tente outra letra!")
                continue
            guessed += guess
            if guess not in words:
                tries -= 1
                print(f"Você errou... ({tries}) tentativas faltando.")
        elif len(guess) > 1:
            if guess == words:
                print("Você acertou!")
                break
            else:
                tries -= 1
                print(f"Você errou... ({tries}) tentativas faltando.")

    if tries == 0:
        print("As tentativas foram esgotadas... Você perdeu.")


if __name__ == '__main__':
    run_game()
