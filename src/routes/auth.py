from flask import Blueprint, request, jsonify

bp_auth = Blueprint("bp_auth", __name__)

@bp_auth.route('/register', methods=['POST'])
def register():
    pass

@bp_auth.route('/login', methods=['POST'])
def login():
    pass