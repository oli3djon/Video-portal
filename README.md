# video_portal

Современное веб‑приложение на **Flask** для публикации видео с админ‑панелью.

## Возможности
- Публичный каталог видео (красивые карточки, поиск, пагинация).
- Просмотр страницы видео.
- Загрузка видео (через админ‑панель).
- Редактирование описания/заголовка.
- Удаление видео.
- Авторизация админа (Flask‑Login).
- SQLite база (по умолчанию).

## Быстрый старт
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Инициализация (создаст БД и пользователя-админа)
python manage.py init-db
python manage.py create-admin --username admin --password admin123

# Запуск
flask --app app run --debug
```

Откройте: http://127.0.0.1:5000

Логин администратора: используйте данные, созданные командой `create-admin`.

## Настройки окружения (необязательно)
Можно создать файл `.env` или переменные окружения:
- `SECRET_KEY` – секретный ключ Flask
- `UPLOAD_MAX_MB` – максимальный размер файла в мегабайтах (по умолчанию 200)
- `ALLOWED_EXTENSIONS` – список расширений (по умолчанию: mp4, mov, webm, mkv)

## фото
<img width="1902" height="911" alt="image" src="https://github.com/user-attachments/assets/56b6e1a1-78b9-4a27-966a-6c9426d54bef" />




## Структура
```
flask_video_portal/
│── flask_video_portal/
│   │── app/              # Основное приложение
│   │── uploads/          # Папка для загруженных видео
│   │── venv/             # Виртуальное окружение
│   │── manage.py         # Точка запуска
│   │── README.md
│   │── requirements.txt  # Зависимости
│   │── videos.db         # SQLite база данных
app/
│── __init__.py     # Инициализация Flask-приложения
│── auth.py         # Аутентификация / авторизация
│── forms.py        # Flask-WTF формы
│── models.py       # SQLAlchemy модели
│── routes.py       # Основные маршруты
│── utils.py        # Вспомогательные функции
│── static/         # CSS, JS, изображения
│── templates/      # HTML-шаблоны



```
