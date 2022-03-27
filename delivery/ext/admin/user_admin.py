from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla import filters
from flask_admin.actions import action
from delivery.ext.db import models, db
from flask import flash


class UserAdmin(ModelView):
    """Interface admin de user"""

#   colunas que serão exibidas na interface administrativa
    column_list = ["admin", "email", "foto"]

#   modifica o nome de exibição da coluna na interface administrativa
    column_labels = {"email": "User login"}

#   faz busca no banco de dados
    column_searchable_list = ["email"]

#   adiciona filtros de buscas
    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            models.User.email,
            "dominio",
            options=(("gmail", "Gmail"), ("uol", "Uol"))
        ),
    ]

#   define as permissões para alterações na interface administrativa
    can_edit = False
    can_create = True
    can_delete = True

#   cria um menu 
    @action("toggle_admin", "Toggle admin status", "Are you sure?")
    def toggle_admin_status(self, ids):
        users = models.User.query.filter(models.User.id.in_(ids))
        for user in users.all():
            user.admin = not user.admin
        db.session.commit()
        flash(f"{users.count()} usuários alterados com sucesso!", "success")

#   cria um menu 
    @action("send_email", "Send email to all users", "Are you sure?")
    def send_email(self, ids):
        users = models.User.query.filter(models.User.id.in_(ids)).all()
        # 1) redirect para um form para escrever a mensagem do email
        # 2) enviar o email
        flash(f"{len(users)} emails enviados.", "success")
