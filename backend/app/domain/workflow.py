TASK_STATUSES = {
    "TODO",
    "IN_PROGRESS",
    "IN_REVIEW",
    "DONE",
    "CANCELLED",
}


ALLOWED_TRANSITIONS = {
    "TODO": {"IN_PROGRESS", "CANCELLED"},
    "IN_PROGRESS": {"IN_REVIEW", "CANCELLED"},
    "IN_REVIEW": {"DONE", "IN_PROGRESS"},
    "DONE": set(),
    "CANCELLED": set(),
}


def is_valid_transition(current_status: str, new_status: str) -> bool:
    return new_status in ALLOWED_TRANSITIONS.get(current_status, set())