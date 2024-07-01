from app.adapters.orm import UserModel
from app.domain.models import User
from app.extensions import db

class UserRepository:
    def get_user_by_username(self, username):
        user_model = UserModel.query.filter_by(username=username).first()
        if user_model:
            return User(user_model.username, user_model.email, user_model.password_hash)
        return None

    def save_user(self, user):
        user_model = UserModel(username=user.username, email=user.email, password_hash=user.password_hash)
        db.session.add(user_model)
        db.session.commit()
