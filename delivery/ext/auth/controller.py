from werkzeug.security import generate_password_hash, check_password_hash  # noqa
from delivery.ext.db import models, db
from werkzeug.utils import secure_filename
import os
from flask import current_app as app


def create_user(email, passwd, foto, admin=False):
    user = models.User(
        email=email,
        passwd=generate_password_hash(passwd, "pbkdf2:sha256"),
        admin=admin,
        foto=foto
    )
    db.session.add(user)
    db.session.commit()
    return user


def save_user_foto(filename, filestorage):
    """
        Saves user foto in
        ./uploads/
    """
    filename = os.path.join(
        app.config["UPLOAD_FOLDER"],
        secure_filename(filename)
    )
    filestorage.save(filename)
