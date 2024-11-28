from flask import Blueprint, request, jsonify

bp_profile = Blueprint("bp_profile", __name__)

@bp_profile.route('/profile', methods=['GET'])
def profile():
    return jsonify({"path": "profile"})

@bp_profile.route('/profile', methods=['PUT'])
def update_profile():
    return jsonify({"path": "update profile"})