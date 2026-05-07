from app.domain.workflow import (
    TASK_STATUSES,
    is_valid_transition,
)

from app.models.task import Task
from app.models.task_history import TaskHistory

from app.repositories.task_repository import TaskRepository


class TaskService:
    @staticmethod
    def create_task(data):
        task = Task(
            title=data["title"],
            description=data.get("description"),
            priority=data["priority"],
        )

        return TaskRepository.create(task)

    @staticmethod
    def get_tasks():
        return TaskRepository.get_all()

    @staticmethod
    def transition_task(task_id, new_status):
        task = TaskRepository.get_by_id(task_id)

        if not task:
            raise ValueError("Task not found")

        if new_status not in TASK_STATUSES:
            raise ValueError("Invalid status")

        if not is_valid_transition(task.status, new_status):
            raise ValueError(
                f"Cannot transition from {task.status} to {new_status}"
            )

        history = TaskHistory(
            task_id=task.id,
            from_status=task.status,
            to_status=new_status,
        )

        task.status = new_status

        TaskRepository.update()
        TaskRepository.create_history(history)

        return task
    
    @staticmethod
    def delete_task(task_id):
        task = TaskRepository.get_by_id(task_id)

        if not task:
            raise ValueError("Task not found")

        TaskRepository.delete(task_id)