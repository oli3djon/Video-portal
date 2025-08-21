# flask_video_portal

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

## Структура
```
app/
  __init__.py
  models.py
  forms.py
  auth.py
  routes.py
  utils.py
  static/
    css/style.css
    js/app.js
    img/logo.svg
  templates/
    base.html
    index.html
    video_detail.html
    upload_success.html
    admin/
      dashboard.html
      edit_video.html
    auth/
      login.html
uploads/  # сюда сохраняются видео
manage.py
```
