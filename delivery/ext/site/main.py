from flask import Blueprint, flash
from flask import render_template, redirect, request
from flask import current_app
from delivery.ext.site import forms
from delivery.ext.auth import controller
from delivery.ext.db import models
from flask_login import login_user


bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    current_app.logger.debug("Entrei na função main")
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")


@bp.route("/admin")
def admin():
    return render_template("restaurants.html")


@bp.route("/cadastro", methods=['GET', 'POST'])
def signup():
    form = forms.UserForm()
    if form.validate_on_submit():
        foto = request.files.get('foto')
        print(foto.filename)

        if foto:
            controller.save_user_foto(foto.filename, foto)

        user = controller.create_user(
            email=form.email.data,
            passwd=form.passwd.data,
            admin=form.admin.data,
            foto=str(form.email.data) + "-perfil-" + str(foto.filename)
        )
        return redirect("/")

    if request.method == "POST":
        __import__("ipdb").set_trace()
    return render_template("userform.html", form=form)


@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()

        if user and user.passwd == form.passwd.data:
            login_user(user)
            flash(f"Bem vindo {user.email}!")
        else:
            flash("Login inválido!")
        return redirect("/")

    if request.method == "POST":
        __import__("ipdb").set_trace()
    return render_template("loginform.html", form=form)
