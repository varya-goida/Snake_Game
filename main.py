import tkinter as tk
from game_engine import SnakeGame


def main():
    """Точка входа в программу"""
    root = tk.Tk()
    game = SnakeGame(root)

    # Центрирование окна
    root.eval('tk::PlaceWindow . center')

    root.mainloop()


if __name__ == "__main__":
    main()