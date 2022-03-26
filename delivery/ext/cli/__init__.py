import click
from delivery.ext.db import db
from delivery.ext.db import models


def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o banco de dados"""
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """adiciona um novo usuário"""
        user = models.User(email=email, passwd=passwd, admin=admin)
        db.session.add(user)
        db.session.commit()

        click.echo(f"Usuário {email} criado com sucesso")

    @app.cli.command()
    @click.option("--name", "-n")
    def add_category(name):
        """adiciona um novo usuário"""
        category = models.Category(name=name)
        db.session.add(category)
        db.session.commit()

    @app.cli.command()
    def listar_pedidos():
        """Este comando carrega a lista de usuários"""
        # TODO: usar tabulate
        click.echo("lista de pedidos")

    @app.cli.command()
    def list_users():
        """Este comando carrega a lista de pedidos"""
        users = models.User.query.all()
        for user in users:
            click.echo({
                "id": str(user.id),
                "email": str(user.email),
                "passwd": str(user.passwd),
                "admin": str(user.admin)
            })
