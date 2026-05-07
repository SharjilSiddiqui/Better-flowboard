from app.extensions.db import db
from app.models.task import Task
from app.models.task_history import TaskHistory


class TaskRepository:

    @staticmethod
    def create(task: Task):
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def get_all():
        return Task.query.order_by(Task.created_at.desc()).all()

    @staticmethod
    def get_by_id(task_id: str):
        return Task.query.filter_by(id=task_id).first()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def create_history(history: TaskHistory):
        db.session.add(history)
        db.session.commit()
        return history

    @staticmethod
    def delete(task_id):
        task = Task.query.get(task_id)

        if not task:
            return None

        # delete task history first
        TaskHistory.query.filter_by(task_id=task_id).delete()

        # delete task
        db.session.delete(task)

        db.session.commit()

        return task