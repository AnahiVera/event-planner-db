from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from models import db

bp_users = Blueprint("bp_users", __name__)

@bp_users.route('/api/users',  methods=['GET'])
def get_users():

    users = User.query.all()
    users= {user.name for user in users}

    return jsonify({"users": users}), 200

@bp_users.route('/api/users', methods=['POST'])
def add_user():

    name = request.json.get('name')

    if not name:
        return jsonify({"status": "error", "message": "Name is required"}), 422
    
    found = User.query.filter_by(name=name).first()

    if found: 
        return jsonify({"status": "error", "message": "User already exists"}), 422
    
    user = User()
    user.name = name

    db.session.add(user)
    db.session.commit()

    return jsonify({"status": "success", "message": "User added successfully"}), 201