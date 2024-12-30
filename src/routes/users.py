from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

bp_users = Blueprint("bp_users", __name__)

@bp_users.route('/users',  methods=['GET'])
def get_users():

    users = User.query.all()
    users= [user.email for user in users]

    return jsonify({"users": users}), 200


@bp_users.route('/users', methods=['POST'])
def add_user():

    email = request.json.get('email')

    if not email:
        return jsonify({"status": "error", "message": "email is required"}), 422
    
    found = User.query.filter_by(email=email).first()

    if found: 
        return jsonify({"status": "error", "message": "email already exists"}), 422
    
    user = User()
    user.email = email

    db.session.add(user)
    db.session.commit()

    return jsonify({"status": "success", "message": "User added successfully"}), 201