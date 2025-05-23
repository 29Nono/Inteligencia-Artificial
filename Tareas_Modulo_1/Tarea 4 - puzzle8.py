import tkinter as tk
import random
from tkinter import messagebox

class PuzzleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de Puzzle")
        self.size = 4
        self.empty_row = self.size - 1
        self.empty_col = self.size - 1
        self.values = [[(i * self.size + j + 1) % (self.size * self.size) for j in range(self.size)] for i in range(self.size)]
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.create_widgets()
        self.shuffle_puzzle()

    def create_widgets(self):
        for i in range(self.size):
            for j in range(self.size):
                text = "" if (i == self.size - 1 and j == self.size - 1) else str(self.values[i][j])
                button = tk.Button(self.master, text=text, font=("Arial", 40), command=lambda row=i, col=j: self.move(row, col))
                button.grid(row=i, column=j, sticky="nsew")
                self.buttons[i][j] = button

        reset_button = tk.Button(self.master, text="Reiniciar", command=self.reset_game)
        reset_button.grid(row=self.size, column=0, columnspan=self.size, sticky="nsew")

        for i in range(self.size):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def shuffle_puzzle(self):
        for _ in range(100):
            direction = random.randint(0, 3)
            if direction == 0: self.move(self.empty_row - 1, self.empty_col)  # Arriba
            elif direction == 1: self.move(self.empty_row + 1, self.empty_col)  # Abajo
            elif direction == 2: self.move(self.empty_row, self.empty_col - 1)  # Izquierda
            elif direction == 3: self.move(self.empty_row, self.empty_col + 1)  # Derecha

    def move(self, new_row, new_col):
        if (0 <= new_row < self.size and 0 <= new_col < self.size and
                ((abs(new_row - self.empty_row) == 1 and new_col == self.empty_col) or
                 (abs(new_col - self.empty_col) == 1 and new_row == self.empty_row))):
            self.buttons[self.empty_row][self.empty_col].config(text=self.buttons[new_row][new_col]['text'])
            self.values[self.empty_row][self.empty_col], self.values[new_row][new_col] = self.values[new_row][new_col], self.values[self.empty_row][self.empty_col]
            self.buttons[new_row][new_col].config(text="")
            self.empty_row, self.empty_col = new_row, new_col
            self.check_win()

    def check_win(self):
        count = 1
        for i in range(self.size):
            for j in range(self.size):
                if i == self.size - 1 and j == self.size - 1:
                    if self.values[i][j] != 0:
                        return
                else:
                    if self.values[i][j] != count:
                        return
                count += 1
        messagebox.showinfo("¡Ganaste!", "¡Felicidades, has ganado!")

    def reset_game(self):
        self.empty_row = self.size - 1
        self.empty_col = self.size - 1
        self.values = [[(i * self.size + j + 1) % (self.size * self.size) for j in range(self.size)] for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                text = "" if (i == self.size - 1 and j == self.size - 1) else str(self.values[i][j])
                self.buttons[i][j].config(text=text)

        self.shuffle_puzzle()

if __name__ == "__main__":
    root = tk.Tk()
    game = PuzzleGame(root)
    root.mainloop()
