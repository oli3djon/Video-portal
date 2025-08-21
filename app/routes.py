import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory, current_app
from flask_login import login_required
from sqlalchemy import desc
from . import db
from .models import Video
from .forms import VideoForm
from .utils import allowed_file, save_upload

bp = Blueprint("main", __name__, template_folder="templates")

@bp.app_template_filter("filesize")
def filesize_filter(path):
    try:
        size = os.path.getsize(path)
        for unit in ['B','KB','MB','GB']:
            if size < 1024.0:
                return f"{size:3.1f} {unit}"
            size /= 1024.0
    except Exception:
        return "-"

@bp.route("/")
def index():
    q = request.args.get("q", "").strip()
    page = int(request.args.get("page", 1))
    per_page = 8
    query = Video.query.order_by(desc(Video.created_at))
    if q:
        query = query.filter(Video.title.ilike(f"%{q}%"))
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template("index.html", pagination=pagination, q=q)

@bp.route("/video/<int:video_id>")
def video_detail(video_id):
    v = Video.query.get_or_404(video_id)
    return render_template("video_detail.html", v=v)

@bp.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename)

# ---------- Admin ----------
from flask_login import login_required

@bp.route("/admin")
@login_required
def admin_dashboard():
    page = int(request.args.get("page", 1))
    per_page = 12
    pagination = Video.query.order_by(Video.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
    return render_template("admin/dashboard.html", pagination=pagination)

@bp.route("/admin/new", methods=["GET", "POST"])
@login_required
def admin_new():
    form = VideoForm()
    if form.validate_on_submit():
        file = form.file.data
        if not file or not allowed_file(file.filename):
            flash("Пожалуйста, выберите видео допустимого формата.", "warning")
            return render_template("admin/edit_video.html", form=form, mode="new")
        saved = save_upload(file)
        v = Video(title=form.title.data, description=form.description.data, filename=saved, original_name=file.filename)
        db.session.add(v)
        db.session.commit()
        flash("Видео загружено!", "success")
        return redirect(url_for("main.admin_dashboard"))
    return render_template("admin/edit_video.html", form=form, mode="new")

@bp.route("/admin/edit/<int:video_id>", methods=["GET", "POST"])
@login_required
def admin_edit(video_id):
    v = Video.query.get_or_404(video_id)
    form = VideoForm(obj=v)
    if request.method == "POST" and form.validate_on_submit():
        v.title = form.title.data
        v.description = form.description.data
        file = form.file.data
        if file and allowed_file(file.filename):
            # удалить старый файл
            try:
                os.remove(os.path.join(current_app.config["UPLOAD_FOLDER"], v.filename))
            except OSError:
                pass
            v.filename = save_upload(file)
            v.original_name = file.filename
        db.session.commit()
        flash("Изменения сохранены.", "success")
        return redirect(url_for("main.admin_dashboard"))
    return render_template("admin/edit_video.html", form=form, mode="edit", v=v)

@bp.route("/admin/delete/<int:video_id>", methods=["POST"])
@login_required
def admin_delete(video_id):
    v = Video.query.get_or_404(video_id)
    # удаляем файл
    try:
        os.remove(os.path.join(current_app.config["UPLOAD_FOLDER"], v.filename))
    except OSError:
        pass
    db.session.delete(v)
    db.session.commit()
    flash("Видео удалено.", "info")
    return redirect(url_for("main.admin_dashboard"))
