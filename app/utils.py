import os, secrets
from flask import current_app
from werkzeug.utils import secure_filename

def allowed_file(filename):
    ext = filename.rsplit('.', 1)[-1].lower()
    return '.' in filename and ext in current_app.config["ALLOWED_EXTENSIONS"]

def save_upload(file_storage):
    # генерация уникального имени и сохранение
    filename = secure_filename(file_storage.filename)
    base, ext = os.path.splitext(filename)
    unique = secrets.token_hex(8)
    final_name = f"{base}-{unique}{ext}"
    path = os.path.join(current_app.config["UPLOAD_FOLDER"], final_name)
    file_storage.save(path)
    return final_name
