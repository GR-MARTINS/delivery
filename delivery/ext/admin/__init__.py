from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from delivery.ext.admin import user_admin
from delivery.ext.db import models  # noqa
from delivery.ext.db import db

admin = Admin()


def init_app(app):
    admin.name = "Delivery Foods"
    admin.template_mode = "bootstrap2"
    admin.init_app(app)

    admin.add_view(user_admin.UserAdmin(models.User, db.session))
    admin.add_view(ModelView(models.Address, db.session))
    admin.add_view(ModelView(models.Store, db.session))
    admin.add_view(ModelView(models.Items, db.session))
    admin.add_view(ModelView(models.Category, db.session))
