import tkinter as tk
from constants import *


class UIManager:
    def __init__(self, root):
        self.root = root

        # Canvas для отрисовки игры
        self.canvas = tk.Canvas(
            self.root,
            width=WIDTH,
            height=HEIGHT,
            bg=GROUND_COLOR,
            highlightthickness=0
        )
        self.canvas.pack()

    def clear_canvas(self):
        """Очистить canvas и удалить все кнопки"""
        self.canvas.delete("all")
        # Удаление всех кнопок
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

    def draw_start_screen(self, start_command, exit_command):
        """Нарисовать стартовый экран"""
        # Заголовок
        self.canvas.create_text(
            WIDTH // 2, 50,
            text="ИГРА ЗМЕЙКА НА PYTHON <3",
            fill=SNAKE_COLOR,
            font=("Arial", 24, "bold")
        )

        # Кнопки
        start_button = tk.Button(
            self.root,
            text="ИГРАТЬ",
            command=start_command,
            bg=MENU_BG,
            fg=MENU_TEXT,
            font=("Arial", 14),
            width=15,
            height=2
        )
        self.canvas.create_window(
            WIDTH // 2, 150,
            window=start_button
        )

        exit_button = tk.Button(
            self.root,
            text="ВЫХОД",
            command=exit_command,
            bg=MENU_BG,
            fg=MENU_TEXT,
            font=("Arial", 14),
            width=15,
            height=2
        )
        self.canvas.create_window(
            WIDTH // 2, 220,
            window=exit_button
        )

    def draw_snake(self, snake):
        """Нарисовать змейку"""
        for segment in snake:
            x, y = segment
            self.canvas.create_rectangle(
                x, y, x + SNAKE_SIZE, y + SNAKE_SIZE,
                fill=SNAKE_COLOR,
                outline=SNAKE_COLOR
            )

    def draw_food(self, food):
        """Нарисовать еду"""
        x, y = food
        self.canvas.create_rectangle(
            x, y, x + SNAKE_SIZE, y + SNAKE_SIZE,
            fill=EAT_COLOR,
            outline=EAT_COLOR
        )

    def draw_game_ui(self, score, player_name, difficulty):
        """Нарисовать игровой UI"""
        # Счет
        self.canvas.create_text(
            60, 20,
            text=f"Счёт: {score}",
            fill=TXT_COLOR,
            font=("Arial", 12, "bold"),
            anchor="w"
        )

        # Имя игрока
        self.canvas.create_text(
            60, 40,
            text=f"Игрок: {player_name}",
            fill=TXT_COLOR,
            font=("Arial", 12),
            anchor="w"
        )

        # Скорость
        self.canvas.create_text(
            60, 60,
            text=f"Скорость: {difficulty}",
            fill=TXT_COLOR,
            font=("Arial", 12),
            anchor="w"
        )

        # Подсказки
        self.canvas.create_text(
            WIDTH // 2, HEIGHT - 20,
            text="Управление: WASD/Стрелки, ESC-меню",
            fill=TXT_COLOR,
            font=("Arial", 10)
        )

    def draw_game_over_screen(self, score, player_name, restart_command, menu_command):
        """Нарисовать экран завершения игры"""
        # Сообщение о завершении игры
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 3,
            text=f"ИГРА ЗАВЕРШЕНА! ВАШ СЧЁТ: {score}",
            fill=EAT_COLOR,
            font=("Arial", 20, "bold")
        )

        # Имя игрока
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 3 + 40,
            text=f"Игрок: {player_name}",
            fill=BLUE,
            font=("Arial", 16)
        )

        # Кнопки
        restart_button = tk.Button(
            self.root,
            text="ИГРАТЬ СНОВА (C)",
            command=restart_command,
            bg=MENU_BG,
            fg=MENU_TEXT,
            font=("Arial", 12),
            width=20
        )
        self.canvas.create_window(
            WIDTH // 2, HEIGHT // 2 + 40,
            window=restart_button
        )

        menu_button = tk.Button(
            self.root,
            text="В МЕНЮ (Q)",
            command=menu_command,
            bg=MENU_BG,
            fg=MENU_TEXT,
            font=("Arial", 12),
            width=20
        )
        self.canvas.create_window(
            WIDTH // 2, HEIGHT // 2 + 90,
            window=menu_button
        )

        # Привязка клавиш для экрана завершения
        self.root.bind("<KeyPress-c>", lambda e: restart_command())
        self.root.bind("<KeyPress-C>", lambda e: restart_command())
        self.root.bind("<KeyPress-q>", lambda e: menu_command())
        self.root.bind("<KeyPress-Q>", lambda e: menu_command())