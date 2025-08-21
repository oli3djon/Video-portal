from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, FileField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired(), Length(max=80)])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Войти")

class VideoForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired(), Length(max=200)])
    description = TextAreaField("Описание")
    file = FileField("Видео файл")
    submit = SubmitField("Сохранить")
