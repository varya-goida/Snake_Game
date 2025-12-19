FROM python:3.9

# Метаданные
LABEL maintainer="your-email@example.com"
LABEL version="1.0"
LABEL description="Snake Game in Python"

# Устанавливаем tkinter
RUN apt-get update && apt-get install -y python3-tk && rm -rf /var/lib/apt/lists/*

# Создаем директорию приложения
WORKDIR /app

# Копируем файлы
COPY snake_game/ ./snake_game/
COPY main.py ./
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем игру
CMD ["python", "main.py"]
