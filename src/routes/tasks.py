from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Task, Event ,db

bp_tasks = Blueprint("bp_tasks", __name__)

@bp_tasks.route('/tasks/<int:event_id>', methods=['GET'])
@jwt_required()
def get_tasks(event_id):

    current_user_id = get_jwt_identity()
    event = Event.query.filter_by(id=event_id, user_id=current_user_id).first()

    if not event:
        return jsonify({"status": "error", "message": "Event not found"}), 404
    
    tasks = Task.query.filter_by(id=event_id).all()

    tasks_json = [task.serialize() for task in tasks]

    return jsonify({tasks_json}), 200

@bp_tasks.route('/tasks/<int:event_id>', methods=['POST'])
@jwt_required()
def add_task(event_id):

    current_user_id = get_jwt_identity()
    event = Event.query.filter_by(id=event_id, user_id=current_user_id).first()

    if not event:
        return jsonify({"status": "error", "message": "Event not found"}), 404
    

    data = request.get_json()
    title = data.get('title')
    status = data.get('status', 'pending')  # Por defecto es 'pending'
    assigned_to = data.get('assigned_to')  # ID del usuario asignado
    due_date = data.get('due_date')

    if not title:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = Task(
        event_id=event_id,
        title=title,
        status=status == 'completed',  # Convert to boolean
        assigned_to=assigned_to,
        due_date=due_date
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.serialize()), 201

@bp_tasks.route('/tasks/<int:task_id>', methods=['PATCH'])
@jwt_required()
def update_task(task_id):

    current_user_id = get_jwt_identity()
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"status": "error", "message": "Task not found"}), 404
    
    event= Event.query.filter_by(id=task.event_id, user_id=current_user_id).first()

    if not event:
        return jsonify({"status": "error", "message": "Event not found"}), 404
    
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.status = data.get('status', 'pending') == 'completed'
    task.assigned_to = data.get('assigned_to', task.assigned_to)
    task.due_date = data.get('due_date', task.due_date)

    db.session.commit()

    return jsonify(task.serialize()), 200

@bp_tasks.route('/tasks', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):

    current_user_id = get_jwt_identity()
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"status": "error", "message": "Task not found"}), 404
    
    event = Event.query.filter_by(id=task.event_id, user_id=current_user_id).first()
    if not event:
        return jsonify({"status": "error", "message": "Event not found"}), 404  
    
    db.session.delete(task)
    db.session.commit()

    return jsonify({"status": "success", "message": "Task deleted"}), 200