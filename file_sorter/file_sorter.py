import os
import shutil
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from customtkinter import CTkLabel, CTkButton


class FileSorter:
    """
    Uma classe para organizar arquivos em subpastas com base em suas extensões.
    """

    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Organizador de Arquivos")
        self.window.geometry("360x130")
        self.window.resizable(False, False)

        self.padding: dict = {"padx": 20, "pady": 10}

        self.title_label = CTkLabel(self.window, text="Selecione o diretório onde deseja organizar os arquivos")
        self.title_label.grid(row=0, column=0, **self.padding)

        self.open_folder_button = CTkButton(self.window, text="Abrir Pasta", command=self.open_folder)
        self.open_folder_button.grid(row=1, column=0, **self.padding)

    def open_folder(self) -> None:
        """
        Abre uma caixa de diálogo para selecionar um diretório e, em seguida, inicia o processo de organização de arquivos.
        """
        directory = filedialog.askdirectory()
        if directory:
            if os.path.exists(directory):
                try:
                    self.sort_files(directory)
                    self.remove_empty_folders(directory)
                    CTkMessagebox(title="Concluído", message=f"Arquivos do diretório '{directory}' foram organizados com sucesso")
                except Exception as e:
                    CTkMessagebox(title="Error", message=f"Ocorreu um erro ao organizar os arquivos: {str(e)}")

    def create_folder(self, path: str, extension: str) -> str:
        """
        Cria uma subpasta com base na extensão do arquivo e retorna o caminho para a subpasta criada.

        :param path: Caminho do diretório pai.
        :param extension: Extensão do arquivo.
        :return: Caminho da subpasta criada.
        """
        folder_name: str = extension[1:]
        folder_path: str = os.path.join(path, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        return folder_path

    def sort_files(self, source_path: str) -> None:
        """
        Organiza os arquivos no diretório de origem em subpastas com base em suas extensões.

        :param source_path: Caminho do diretório de origem.
        """
        for root_dir, sub_dir, filenames in os.walk(source_path):
            for filename in filenames:
                file_path: str = os.path.join(root_dir, filename)
                extension: str = os.path.splitext(filename)[1]

                if extension:
                    target_folder: str = self.create_folder(source_path, extension)
                    target_path: str = os.path.join(target_folder, filename)

                    shutil.move(file_path, target_path)

    def remove_empty_folders(self, source_path: str) -> None:
        """
        Remove pastas vazias no diretório de origem.

        :param source_path: Caminho do diretório de origem.
        """
        for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
            for current_dir in sub_dir:
                folder_path: str = os.path.join(root_dir, current_dir)

                if not os.listdir(folder_path):
                    os.rmdir(folder_path)


if __name__ == '__main__':
    file_sorter = FileSorter()
    file_sorter.window.mainloop()
