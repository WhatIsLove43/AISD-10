import tkinter as tk
from tkinter import messagebox
import random
import time


class TicTacToe:
    def __init__(self):
        self.root = root
        self.root.title("Крестики-нолики")

        # Игровое поле: 3x3 кнопки
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Инициализация интерфейса
        self.current_player = "X"  # Игрок всегда "X"
        self.create_buttons()

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 300
        window_height = 300

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_buttons(self):
    # Создает игровое поле с кнопками
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                    command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_click(self, row, col):
    # Обрабатывает нажатие игроком на клетку
        if self.buttons[row][col]["text"] == "" and self.check_winner() is None:
        # Ход игрока
            self.buttons[row][col]["text"] = "X"
            self.board[row][col] = "X"

            if self.check_winner() == "X":
                messagebox.showinfo("Победа!", "Вы выиграли!")
                self.reset_board()
            elif not self.is_moves_left():
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_board()
            else:
                # Ход компьютера
                self.computer_move()

    def computer_move(self):
    # Логика хода компьютера (непроигрывающий алгоритм)
        best_score = -float('inf')
        best_move = None

        # Минимакс для нахождения оптимального хода
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    score = self.minimax(False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        # Выполняем лучший ход
        if best_move:
            i, j = best_move
            self.buttons[i][j]["text"] = "O"
            self.board[i][j] = "O"

            if self.check_winner() == "O":
                messagebox.showinfo("Поражение", "Компьютер выиграл!")
                self.reset_board()
            elif not self.is_moves_left():
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_board()

    def minimax(self, is_maximizing):
    # Реализация алгоритма Минимакс#
        winner = self.check_winner()
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif not self.is_moves_left():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "":
                        self.board[i][j] = "O"
                        score = self.minimax(False)
                        self.board[i][j] = ""
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "":
                        self.board[i][j] = "X"
                        score = self.minimax(True)
                        self.board[i][j] = ""
                        best_score = min(best_score, score)
            return best_score

    def check_winner(self):
    # Проверяет победителя
        for i in range(3):
        # Проверка строк и столбцов
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != "":
                return self.board[0][i]

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "":
            return self.board[0][2]

        return None

    def is_moves_left(self):
    # Проверяет, остались ли ходы
        for row in self.board:
            if "" in row:
                return True
        return False

    def reset_board(self):
    # Сбрасывает игровое поле
        for i in range(3):
           for j in range(3):
               self.board[i][j] = ""
               self.buttons[i][j]["text"] = ""


if __name__ == "__main__":
    start_time = time.perf_counter()
    root = tk.Tk()
    app = TicTacToe()
    end_time = time.perf_counter()
    final_time = end_time - start_time
    print(f"Время работы программы: {final_time:.2f} секунд")
    root.mainloop()
