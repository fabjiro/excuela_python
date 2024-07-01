from app.services.user_service import UserService
from flask_jwt_extended import create_access_token

class UserUseCases:
    def __init__(self):
        self.user_service = UserService()

    def register_user(self, data):
        return self.user_service.register_user(data['username'], data['email'], data['password'])

    def login_user(self, data):
        user = self.user_service.authenticate_user(data['username'], data['password'])
        if user:
            access_token = create_access_token(identity={'username': user.username, 'email': user.email})
            return {"access_token": access_token}, 200
        return {"error": "Invalid credentials"}, 401
