import random
import sys
from typing import Dict, List


class PPT:
    def __init__(self):
        """
        Inicializa o jogo 'Pedra, Papel ou Tesoura'.
        """
        print("Bem vindo ao jogo 'Pedra, Papel ou Tesoura!'")
        self.score_user: int = 0
        self.score_robot: int = 0
        self.min_score_to_win: int = 5

        self.moves: Dict[str, str] = {"pedra": "🪨", "papel": "📜", "tesoura": "✂️"}
        self.valid_moves: List[str] = list(self.moves.keys())

    def play_game(self):
        """
        Inicia o jogo e permite que o usuário jogue até que um dos jogadores alcance a pontuação mínima.
        """
        while True:
            user_move: str = input("Pedra, papel ou tesoura? >> ").lower()

            if user_move == "sair":
                print(f"Obrigado por jogar! Placar final: Você {self.score_user} x {self.score_robot} Robô")
                sys.exit()

            if user_move not in self.valid_moves:
                print("Jogada Inválida! Por favor, insira uma jogada válida...")
                continue

            ia_move: str = random.choice(self.valid_moves)

            self.display_moves(user_move, ia_move)
            result = self.check_move(user_move, ia_move)
            self.update_score(result)

            if self.score_user >= self.min_score_to_win or self.score_robot >= self.min_score_to_win:
                print(f"Placar final: Você {self.score_user} x {self.score_robot} Robô")
                sys.exit()

    def display_moves(self, user_move: str, ia_move: str):
        """
        Exibe as jogadas do usuário e do robô.
        """
        print("|||||||||||||")
        print(f"Você: {self.moves[user_move]}")
        print(f"Robô: {self.moves[ia_move]}")
        print("|||||||||||||")

    def check_move(self, user_move: str, ia_move: str) -> str:
        """
        Verifica o resultado da rodada.

        Args:
            user_move (str): A jogada do usuário.
            ia_move (str): A jogada do robô.

        Returns:
            str: O resultado da rodada ("user" para vitória do jogador, "robot" para vitória do robô, "empate" para empate).
        """
        if user_move == ia_move:
            print("Empate!")
            return "empate"
        elif (user_move == "pedra" and ia_move == "tesoura") or \
                (user_move == "tesoura" and ia_move == "papel") or \
                (user_move == "papel" and ia_move == "pedra"):
            print("Você ganhou!")
            return "user"
        else:
            print("Robô ganhou...")
            return "robot"

    def update_score(self, result: str):
        """
        Atualiza a pontuação com base no resultado da rodada.

        Args:
            result (str): O resultado da rodada ("user" para vitória do jogador, "robot" para vitória do robô, "empate" para empate).
        """
        if result == "user":
            self.score_user += 1
        elif result == "robot":
            self.score_robot += 1

        print(f"Placar: Você {self.score_user} x {self.score_robot} Robô")


if __name__ == '__main__':
    game = PPT()
    game.play_game()
