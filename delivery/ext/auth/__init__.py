from delivery.ext.db import models  # noqa
from flask_login import LoginManager


lm = LoginManager()


def init_app(app):
    """TODO: inicializar Flask Simple Login + JWT"""
    lm.init_app(app)


@lm.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)
