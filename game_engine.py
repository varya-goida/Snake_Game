import tkinter as tk
from constants import *
from ui_manager import UIManager
from dialogs import GameDialogs
import random


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("ИГРА ЗМЕЙКА")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.resizable(False, False)

        # Основные переменные игры
        self.snake = []
        self.food = [0, 0]
        self.direction = "Right"
        self.next_direction = "Right"
        self.score = 0
        self.length = 1
        self.game_running = False
        self.game_over = False

        # Менеджеры
        self.ui = UIManager(self.root)
        self.dialogs = GameDialogs(self.root)

        # Отображение стартового экрана
        self.show_start_screen()

    def show_start_screen(self):
        """Показать стартовый экран"""
        self.ui.clear_canvas()
        self.ui.draw_start_screen(self.start_game_dialog, self.root.quit)

    def start_game_dialog(self):
        """Запуск диалогов перед игрой"""
        global player_name, default_player_name

        # Получение имени игрока
        name = self.dialogs.get_player_name()
        if name:
            player_name = name
            default_player_name = False

            # Получение уровня сложности
            diff = self.dialogs.get_difficulty()
            if diff:
                global difficulty
                difficulty = diff
                self.start_game()

    def start_game(self):
        """Начать новую игру"""
        self.ui.clear_canvas()

        # Инициализация игры
        self.snake = [[WIDTH // 2, HEIGHT // 2]]
        self.food = self.generate_food()
        self.direction = "Right"
        self.next_direction = "Right"
        self.score = 0
        self.length = 1
        self.game_running = True
        self.game_over = False

        # Фокусировка на canvas для обработки клавиш
        self.ui.canvas.focus_set()

        # Привязка клавиш
        self.root.bind("<KeyPress>", self.on_key_press)

        # Запуск игрового цикла
        self.game_loop()

    def generate_food(self):
        """Сгенерировать новую еду"""
        x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
        y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0
        return [x, y]

    def on_key_press(self, event):
        """Обработка нажатий клавиш"""
        if not self.game_running:
            return

        key = event.keysym

        # Изменение направления с проверкой на противоположное
        if key in ("Left", "a", "A") and self.direction != "Right":
            self.next_direction = "Left"
        elif key in ("Right", "d", "D") and self.direction != "Left":
            self.next_direction = "Right"
        elif key in ("Up", "w", "W") and self.direction != "Down":
            self.next_direction = "Up"
        elif key in ("Down", "s", "S") and self.direction != "Up":
            self.next_direction = "Down"
        elif key == "Escape":
            self.game_over = True
            self.show_game_over_screen()

    def update_snake_position(self):
        """Обновить позицию змейки"""
        head_x, head_y = self.snake[-1]

        self.direction = self.next_direction

        if self.direction == "Left":
            head_x -= SNAKE_SIZE
        elif self.direction == "Right":
            head_x += SNAKE_SIZE
        elif self.direction == "Up":
            head_y -= SNAKE_SIZE
        elif self.direction == "Down":
            head_y += SNAKE_SIZE

        # Проверка столкновения с границами
        if (head_x < 0 or head_x >= WIDTH or
                head_y < 0 or head_y >= HEIGHT):
            self.game_over = True
            self.show_game_over_screen()
            return False

        # Добавление новой головы
        new_head = [head_x, head_y]

        # Проверка столкновения с собой
        if new_head in self.snake:
            self.game_over = True
            self.show_game_over_screen()
            return False

        self.snake.append(new_head)

        # Проверка поедания еды
        if (abs(head_x - self.food[0]) < SNAKE_SIZE and
                abs(head_y - self.food[1]) < SNAKE_SIZE):
            self.score += 1
            self.length += 1
            self.food = self.generate_food()
        else:
            # Удаление хвоста если не съели еду
            if len(self.snake) > self.length:
                self.snake.pop(0)

        return True

    def game_loop(self):
        """Основной игровой цикл"""
        if not self.game_running or self.game_over:
            return

        # Очистка canvas
        self.ui.clear_canvas()

        # Обновление позиции змейки
        if not self.update_snake_position():
            return

        # Отрисовка
        self.ui.draw_food(self.food)
        self.ui.draw_snake(self.snake)
        self.ui.draw_game_ui(self.score, player_name, difficulty)

        # Продолжение цикла
        if self.game_running and not self.game_over:
            self.root.after(1000 // difficulty, self.game_loop)

    def show_game_over_screen(self):
        """Показать экран завершения игры"""
        self.game_running = False
        self.ui.clear_canvas()

        # Отображение экрана завершения
        self.ui.draw_game_over_screen(
            self.score,
            player_name,
            self.start_game,
            self.show_start_screen
        )