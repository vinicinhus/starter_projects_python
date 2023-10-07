"""
Instale as seguintes bibliotecas, para o código funcionar:
    pip install customtkinter == 5.2.0
"""

import customtkinter as ctk


class TaxCalculator:
    """
    Uma calculadora simples para calcular taxas com base na renda e na porcentagem.
    """

    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Calculador de Taxas")
        self.window.geometry("300x300")
        self.window.resizable(False, False)

        self.padding: dict = {"padx": 20, "pady": 10}

        self.income_label = ctk.CTkLabel(self.window, text="Renda:")
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        self.tax_rate_label = ctk.CTkLabel(self.window, text="Porcentagem:")
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        self.result_label = ctk.CTkLabel(self.window, text="Taxa:")
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, "0")
        self.result_entry.grid(row=2, column=1, **self.padding)

        self.calculate_button = ctk.CTkButton(self.window, text="Calcular", command=self.calculate_tax)
        self.calculate_button.grid(row=3, column=1, **self.padding)

    def update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        """
        Calcula a taxa com base na renda e na porcentagem inseridas e exibe o resultado.
        """
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            self.update_result(f"R${income * (tax_rate / 100):,.2f}")
        except ValueError:
            self.update_result("Input Inválido")

    def run(self):
        """
        Executa a interface gráfica da calculadora de taxas.
        """
        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()
