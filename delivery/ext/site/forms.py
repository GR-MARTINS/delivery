import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField


class UserForm(FlaskForm):
    email = wtf.EmailField(
        "E-mail", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    passwd = wtf.PasswordField(
        "Senha", [wtf.validators.DataRequired()]
    )
    admin = wtf.BooleanField(
        "Admin", [wtf.validators.DataRequired()]
    )
    foto = FileField("Foto")


class LoginForm(FlaskForm):
    email = wtf.EmailField(
        "E-mail", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    passwd = wtf.PasswordField(
        "Senha", [wtf.validators.DataRequired()]
    )
