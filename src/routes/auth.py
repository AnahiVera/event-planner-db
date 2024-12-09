import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

bp_auth = Blueprint("bp_auth", __name__)

@bp_auth.route('/register', methods=['POST'])
def register():
    
    email = request.json.get('email')
    password = request.json.get('password')

    if not email:
        return jsonify({"message": "Email is required"}), 422
    
    if not password:
        return jsonify({"message": "Password is required"}), 422


@bp_auth.route('/login', methods=['POST'])
def login():
    return jsonify({"path": "login"})