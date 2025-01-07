from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Event,User,db
from datetime import datetime

bp_event = Blueprint("bp_event", __name__)

@bp_event.route('/event', methods=['GET'])
@jwt_required()
def get_events():

    current_user_id = get_jwt_identity() 
    events = Event.query.filter_by(user_id=current_user_id).all()

    events_json = [event.serialize() for event in events]

    return jsonify({events_json}), 200

@bp_event.route('/event', methods=['POST'])
@jwt_required()
def add_event():

    current_user_id = get_jwt_identity() 
    data = request.get_json()
    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"status": "error", "message": "User is not authorized"}), 401
    
    title = data.get('title')
    description = data.get('description')
    date = data.get('date')
    location = data.get('location')
    organizer_id = data.get('organizer_id')
    created_at = data.get('created_at', datetime.now())
    updated_at = data.get('updated_at', datetime.now())

    if not title or not date:
        return jsonify({"error": "Title and date are required"}), 400


    new_event = Event(
        title=title,
        description=description,
        date=date,
        location=location,
        organizer_id=organizer_id,
        created_at=created_at,
        updated_at=updated_at   
    )

    db.session.add(new_event)
    db.session.commit()

    return jsonify({"status": "success", "message": "Event added successfully"}), 201

@bp_event.route('/event', methods=['PATCH'])
@jwt_required()
def update_event(event_id):

    current_user_id = get_jwt_identity() 
    event = Event.query.filter_by(id=event_id, user_id=current_user_id).first()

    if not event:
        return jsonify({"status": "error", "message": "Event not found"}), 404
    
    data = request.get_json()

    event.title = data.get('title', event.title)
    event.description = data.get('description', event.description)
    event.date = data.get('date', event.date)
    event.location = data.get('location', event.location)
    event.updated_at = data.get('updated_at', event.updated_at)

    db.session.commit()

    return jsonify(event.serialize()), 200

@bp_event.route('/event', methods=['DELETE'])
@jwt_required()
def delete_event(event_id):
    current_user_id = get_jwt_identity()
    event = Event.query.filter_by(id=event_id, user_id=current_user_id).first()

    if not event:
        return jsonify({"error": "Event not found or not authorized"}), 404

    db.session.delete(event)
    db.session.commit()

    return jsonify({"message": "Event deleted succesfully"}), 200