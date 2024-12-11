from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

bp_event = Blueprint("bp_event", __name__)

@bp_event.route('/event', methods=['GET'])
def addEvent():
    return jsonify({"path": "event"})

@bp_event.route('/event', methods=['PATCH'])
def update_event():
    return jsonify({"path": "update event"})

@bp_event.route('/event', methods=['DELETE'])
def delete_event():
    return jsonify({"path": "delete event"})