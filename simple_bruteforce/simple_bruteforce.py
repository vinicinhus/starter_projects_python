"""
Esse código é apenas para demonstração de um simples código de bruteforce, portanto não está com as melhores práticas
para executa-lo.

WARNING: O código deixa salvo todas as senhas percorridas na memória, logo se o input da senha for uma senha dificil ou
         com muitos caracteres a memória do computador pode chegar a 99% resultando em lentidão no computador.
"""

import concurrent.futures
import itertools
import string
import time


def common_guess(word: str) -> str | None:
    """
    Verifica se a senha inserida é uma senha comum a partir de uma lista de senhas comuns.

    Args:
        word (str): A senha a ser verificada.

    Returns:
        str | None: Retorna a senha comum encontrada ou None se não encontrar.
    """
    with open("wordlist.txt") as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f"Senha comum encontrada: {match} (#{i})"


def brute_force_worker(word: str, chars: str, length: int, digits: bool, symbols: bool, start, end) -> str | None:
    """
    Função auxiliar para realizar a busca por força bruta em um intervalo específico.

    Args:
        word (str): A senha alvo.
        chars (str): O conjunto de caracteres para tentativas.
        length (int): O comprimento da senha.
        digits (bool): Se deve incluir dígitos na busca.
        symbols (bool): Se deve incluir símbolos na busca.
        start (int): O início do intervalo de tentativas.
        end (int): O fim do intervalo de tentativas.

    Returns:
        str | None: Retorna a senha encontrada ou None se não encontrar.
    """
    attempts: int = 0

    for guess in itertools.islice(itertools.product(chars, repeat=length), start, end):
        attempts += 1
        guess: str = "".join(guess)

        if guess == word:
            return f"{word} foi crackeado em {attempts:,} tentativas."

        if attempts % 100000 == 0:
            print(guess, attempts)


def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    """
    Realiza uma busca por força bruta para encontrar uma senha.

    Args:
        word (str): A senha alvo.
        length (int): O comprimento da senha.
        digits (bool): Se deve incluir dígitos na busca.
        symbols (bool): Se deve incluir símbolos na busca.

    Returns:
        str | None: Retorna a senha encontrada ou None se não encontrar.
    """
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    total_attempts: int = 0
    batch_size: int = 100000  # Ajuste o tamanho do lote conforme necessário

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(0, len(chars) ** length, batch_size):
            start = i
            end = i + batch_size
            futures.append(executor.submit(brute_force_worker, word, chars, length, digits, symbols, start, end))

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                return result


def main():
    password_input: str = input("Insira a sua senha: ")

    start_time: float = time.perf_counter()

    if common_match := common_guess(password_input):
        print(common_match)
    else:
        if cracked := brute_force(password_input, length=len(password_input), digits=False, symbols=False):
            print(cracked)
        else:
            print(f"A Senha {password_input} não foi encontrada...")

    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), "s")


if __name__ == '__main__':
    main()
