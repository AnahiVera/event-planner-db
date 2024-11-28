import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User, Profile
from werkzeug.security import generate_password_hash, check_password_hash

bp_auth = Blueprint("bp_auth", __name__)

@bp_auth.route('/register', methods=['POST'])
def register():
    
    username = request.json.get('username')
    password = request.json.get('password')

    if not username:
        return jsonify({"message": "Username is required"}), 422
    
    if not password:
        return jsonify({"message": "Password is required"}), 422


@bp_auth.route('/login', methods=['POST'])
def login():
    return jsonify({"path": "login"})