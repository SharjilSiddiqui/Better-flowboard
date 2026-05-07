import uuid
from datetime import datetime, UTC

from app.extensions.db import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    title = db.Column(db.String(255), nullable=False)

    description = db.Column(db.Text, nullable=True)

    status = db.Column(
        db.String(50),
        nullable=False,
        default="TODO",
    )

    priority = db.Column(
        db.String(20),
        nullable=False,
        default="MEDIUM",
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC),
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )