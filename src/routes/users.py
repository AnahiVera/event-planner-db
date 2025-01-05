from flask import Blueprint, request, jsonify
from models import User, db


bp_users = Blueprint("bp_users", __name__)

@bp_users.route('/users',  methods=['GET'])
def get_users():

    users = User.query.all()
    users= [user.email for user in users]

    return jsonify({"users": users}), 200

