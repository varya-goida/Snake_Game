import tkinter as tk
from tkinter import simpledialog
from constants import *


class GameDialogs:
    def __init__(self, parent):
        self.parent = parent

    def get_player_name(self):
        """Получить имя игрока через диалог"""
        name = simpledialog.askstring(
            "Имя игрока",
            "Введите ваше имя:",
            parent=self.parent,
            initialvalue="Змеёнышь" if default_player_name else player_name
        )
        return name

    def get_difficulty(self):
        """Получить уровень сложности через диалог"""
        difficulty_dialog = tk.Toplevel(self.parent)
        difficulty_dialog.title("Выбор сложности")
        difficulty_dialog.geometry("500x300")
        difficulty_dialog.resizable(False, False)
        difficulty_dialog.transient(self.parent)
        difficulty_dialog.grab_set()

        tk.Label(
            difficulty_dialog,
            text="Выберите сложность:",
            font=("Arial", 14)
        ).pack(pady=20)

        diff_var = tk.StringVar(value="Средняя")

        difficulties = {
            "Лёгкая": 5,
            "Средняя": 15,
            "Тяжёлая": 30
        }

        for diff_text in difficulties:
            tk.Radiobutton(
                difficulty_dialog,
                text=diff_text,
                variable=diff_var,
                value=diff_text,
                font=("Arial", 12)
            ).pack(anchor='w', padx=50)

        selected_difficulty = [None]  # Используем список для модификации в closure

        def on_confirm():
            selected_difficulty[0] = difficulties[diff_var.get()]
            difficulty_dialog.destroy()

        tk.Button(
            difficulty_dialog,
            text="Начать игру",
            command=on_confirm,
            bg=MENU_BG,
            fg=MENU_TEXT,
            font=("Arial", 12)
        ).pack(pady=20)

        # Ждем закрытия диалога
        self.parent.wait_window(difficulty_dialog)

        return selected_difficulty[0]