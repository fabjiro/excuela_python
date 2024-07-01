from app.adapters.repositories.user_repository import UserRepository
from app.domain.models import User
from app.extensions import bcrypt

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, username, email, password):
        if self.user_repository.get_user_by_username(username):
            return {"error": "Username already exists"}, 400
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username, email, hashed_password)
        self.user_repository.save_user(new_user)
        return {"message": "User registered successfully"}, 201

    def authenticate_user(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        if user and bcrypt.check_password_hash(user.password_hash, password):
            return user
        return None
