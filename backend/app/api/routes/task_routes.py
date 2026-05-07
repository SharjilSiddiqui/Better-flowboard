from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.schemas.task_schema import (
    CreateTaskSchema,
    TransitionTaskSchema,
)

from app.services.task_service import TaskService

task_bp = Blueprint("tasks", __name__)


@task_bp.route("/tasks", methods=["POST"])
def create_task():
    try:
        data = CreateTaskSchema().load(request.json)

        task = TaskService.create_task(data)

        return jsonify({
            "id": task.id,
            "title": task.title,
            "status": task.status,
            "priority": task.priority,
        }), 201

    except ValidationError as err:
        return jsonify({
            "error": err.messages
        }), 400


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = TaskService.get_tasks()

    return jsonify([
        {
            "id": task.id,
            "title": task.title,
            "status": task.status,
            "priority": task.priority,
        }
        for task in tasks
    ])


@task_bp.route("/tasks/<task_id>/transition", methods=["POST"])
def transition_task(task_id):
    try:
        data = TransitionTaskSchema().load(request.json)

        task = TaskService.transition_task(
            task_id,
            data["to_status"],
        )

        return jsonify({
            "id": task.id,
            "status": task.status,
        })

    except ValidationError as err:
        return jsonify({
            "error": err.messages
        }), 400

    except ValueError as err:
        return jsonify({
            "error": str(err)
        }), 400