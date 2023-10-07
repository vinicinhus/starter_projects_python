"""
Instale as seguintes bibliotecas, para o código funcionar:
    pip install requests == 2.31.0
"""

import os

import requests


def get_extension(image_url: str) -> str | None:
    """
    Obtém a extensão de um URL de imagem.

    Args:
        image_url (str): O URL da imagem.

    Returns:
        str | None: A extensão da imagem (por exemplo, '.png') ou None se não for encontrada.
    """
    extensions: list[str] = [".png", ".jpeg", ".jpg", ".gif", ".svg"]

    for extension in extensions:
        if extension in image_url:
            return extension


def download_image(image_url: str, name: str, folder: str):
    """
    Faz o download de uma imagem a partir de uma URL e a salva no diretório especificado.

    Args:
        image_url (str): O URL da imagem a ser baixada.
        name (str): O nome a ser dado à imagem baixada.
        folder (str): O diretório onde a imagem será salva.

    Raises:
        Exception: Se não for possível encontrar a extensão da imagem ou se o nome do arquivo já existir no diretório.
    """
    if extension := get_extension(image_url):
        if folder:
            image_name: str = f"{folder}/{name}{extension}"
        else:
            image_name: str = f"{name}{extension}"
    else:
        raise Exception("Não foi possível encontrar a extensão da imagem...")

    if os.path.isfile(image_name):
        raise Exception(f"O nome do arquivo ({image_name}) já existe no diretório...")

    try:
        image_content: bytes = requests.get(image_url).content

        with open(image_name, "wb") as handler:
            handler.write(image_content)
            print(f"Downloaded: '{image_name}'")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    input_url: str = input("Insira a URL da imagem: ")
    input_image_name: str = input("Insira o nome que deseja colocar na imagem: ")

    print("Downloading...")
    download_image(input_url, name=input_image_name, folder="images")
