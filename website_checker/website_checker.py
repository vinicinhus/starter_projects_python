"""
Instale as seguintes bibliotecas, para o código funcionar:
    pip install requests == 2.31.0
    pip install fake_useragent == 1.3.0
"""

import csv
from http import HTTPStatus

import requests
from fake_useragent import UserAgent


def get_websites(csv_path: str) -> list[str]:
    """
    Lê um arquivo CSV contendo URLs e retorna uma lista de URLs.

    Args:
        csv_path (str): O caminho para o arquivo CSV.

    Returns:
        list[str]: Uma lista de URLs lidas do arquivo CSV.
    """
    websites: list[str] = []

    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if "https://" not in row[0]:
                websites.append(f"https://{row[0]}")
            else:
                websites.append(row[0])

    return websites


def get_user_agent() -> str:
    """
    Gera um User-Agent falso usando a biblioteca fake_useragent e retorna como uma string.

    Returns:
        str: Um User-Agent gerado aleatoriamente.
    """
    ua = UserAgent()
    return ua.chrome


def get_status_description(status_code: int) -> str:
    """
    Retorna a descrição do código de status HTTP.

    Args:
        status_code (int): O código de status HTTP.

    Returns:
        str: A descrição do código de status ou uma mensagem de erro se o código não for encontrado.
    """
    for value in HTTPStatus:
        if value == status_code:
            description: str = f"({value} {value.name}) {value.description}"
            return description

    return "(???) Código de Status HTTPS não encontrado..."


def check_website(website: str, user_agent: str):
    """
    Verifica o status de um website e imprime a URL e a descrição do status.

    Args:
        website (str): A URL do website a ser verificado.
        user_agent (str): O User-Agent a ser usado na solicitação HTTP.
    """
    try:
        response = requests.get(website, headers={"User-Agent": user_agent})
        code: int = response.status_code
        print(website, get_status_description(code))
    except Exception as e:
        print(f"Não foi possível coletar informações do website: '{website}'")
        print(e)


def main():
    sites: list[str] = get_websites("websites.csv")
    user_agent: str = get_user_agent()

    for site in sites:
        check_website(site, user_agent)


if __name__ == '__main__':
    main()
