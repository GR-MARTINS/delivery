from delivery.ext.site.models import User


def get_all_active_users():
    """Get all users"""
    User.db.filter(active=True).all()

