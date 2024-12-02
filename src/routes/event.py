from flask import Blueprint, request, jsonify

bp_event = Blueprint("bp_event", __name__)

@bp_event.route('/event', methods=['GET'])
def event():
    return jsonify({"path": "profile"})

@bp_event.route('/event', methods=['PATCH'])
def update_event():
    return jsonify({"path": "update profile"})