markdown
# Игра Змейка на Python

Классическая игра "Змейка" с графическим интерфейсом на tkinter.
## Архитектура проекта
```plaintext
snake-game/
├── SCR/
│   ├── constants.py
│   ├── game_engine.py
│   ├── ui_manager.py
│   ├── dialogs.py
│   └── __init__.py
├── main.py
├── .pre-commit-config.yaml
├── README.md
├── Dockerfile
└── .gitignore ```
## Особенности
- Выбор уровня сложности (легкий, средний, тяжелый)
- Ввод имени игрока
- Подсчет очков
- Управление с клавиатуры
- Русский интерфейс

## Установка и запуск

### Требования
- Python 3.6 или выше
- Tkinter (обычно входит в стандартную поставку Python)

## Запуск через Docker

### Сборка и запуск образа:
```bash
docker build -t snake-game .
docker run -it --rm snake-game
