from flask import Blueprint, request, jsonify
from models import User, Profile

bp_auth = Blueprint("bp_auth", __name__)

@bp_auth.route('/register', methods=['POST'])
def register():
    return jsonify({"path": "register"})

@bp_auth.route('/login', methods=['POST'])
def login():
    return jsonify({"path": "login"})