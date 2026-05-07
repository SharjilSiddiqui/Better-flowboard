import uuid
from datetime import datetime, UTC

from app.extensions.db import db



class TaskHistory(db.Model):
    __tablename__ = "task_history"

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    task_id = db.Column(
        db.String(36),
        db.ForeignKey("tasks.id"),
        nullable=False,
    )

    from_status = db.Column(
        db.String(50),
        nullable=False,
    )

    to_status = db.Column(
        db.String(50),
        nullable=False,
    )

    changed_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC),
    )