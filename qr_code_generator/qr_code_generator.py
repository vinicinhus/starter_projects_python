"""
Instale as seguintes bibliotecas, para o código funcionar:
    pip install qrcode == 7.4.2
    pip install Pillow == 10.0.1
"""

import qrcode


class QRCodeGenerator:
    def __init__(self, box_size: int, border: int):
        """
        Inicializa um gerador de QR Code.

        Args:
            box_size (int): O tamanho das caixas no QR Code.
            border (int): A largura da borda do QR Code.
        """
        self.qr = qrcode.QRCode(box_size=box_size, border=border)

    def create_qr_code(self, filename: str, foreground_color: str, background_color: str):
        """
        Cria um QR Code a partir de um texto ou URL inserido pelo usuário e salva-o em um arquivo.

        Args:
            filename (str): O nome do arquivo onde o QR Code será salvo.
            foreground_color (str): A cor das caixas do QR Code.
            background_color (str): A cor de fundo do QR Code.
        """
        user_input: str = input("Insira um texto ou uma URL: ")

        try:
            self.qr.add_data(user_input)
            qr_code_image = self.qr.make_image(fill_color=foreground_color, back_color=background_color)
            qr_code_image.save(filename)

            print(f"QR Code gerado! ({filename})")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


def main():
    my_qr_code_generator = QRCodeGenerator(box_size=50, border=10)
    my_qr_code_generator.create_qr_code("qr_code.png", foreground_color="black", background_color="white")


if __name__ == '__main__':
    main()
