from flask import Blueprint, request, jsonify

bp_tasks = Blueprint("bp_tasks", __name__)

@bp_tasks.route('/tasks', methods=['GET'])
def gettask():
    return jsonify({"path": "Get tasks"})

@bp_tasks.route('/tasks', methods=['POST'])
def addtask():
    return jsonify({"path": "Add tasks"})

@bp_tasks.route('/tasks', methods=['PATCH'])
def updatetask():
    return jsonify({"path": "Update task"})

@bp_tasks.route('/tasks', methods=['DELETE'])
def deletetask():
    return jsonify({"path": "Delete task"})