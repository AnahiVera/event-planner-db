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

