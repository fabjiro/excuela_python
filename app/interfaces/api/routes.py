from flask import Blueprint, request, jsonify
from app.use_cases.user_use_cases import UserUseCases
from flask_jwt_extended import jwt_required, get_jwt_identity

main = Blueprint('main', __name__)
user_use_cases = UserUseCases()

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return user_use_cases.register_user(data)

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return user_use_cases.login_user(data)

@main.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    return jsonify(current_user), 200

@main.route('/user', methods=['PUT'])
@jwt_required()
def update_user():
    current_user = get_jwt_identity()
    data = request.get_json()
    # Implementar lógica de actualización del usuario
    return jsonify({"message": "User updated successfully"}), 200

@main.route('/user', methods=['DELETE'])
@jwt_required()
def delete_user():
    current_user = get_jwt_identity()
    # Implementar lógica de eliminación del usuario
    return jsonify({"message": "User deleted successfully"}), 200
