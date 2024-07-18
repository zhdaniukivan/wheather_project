# Используем официальный образ Python в качестве базового
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /weather_project

# Копируем файл зависимостей в контейнер
COPY requirements.txt /weather_project/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения в контейнер
COPY . /weather_project/

# Прописываем команду запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]