from flask import Blueprint, request, jsonify

bp_tasks = Blueprint("bp_tasks", __name__)

@bp_tasks.route('/tasks', methods=['POST'])
def addtask():
    pass