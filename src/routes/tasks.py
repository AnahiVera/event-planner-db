from flask import Blueprint, request, jsonify

tasks = Blueprint("tasks", __name__)

@tasks.route('/tasks', methods=['POST'])
def addtask():
    pass