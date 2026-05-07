# FlowBoard

FlowBoard is a lightweight workflow-based task management system built to demonstrate maintainable full-stack engineering practices, controlled state transitions, validation, testing, and AI-assisted development workflows.

The project focuses on correctness, predictability, and clean architecture rather than feature breadth or UI complexity.

---

# Tech Stack

## Frontend

- React
- TypeScript
- Vite
- React Query
- TailwindCSS
- Axios
- Zod

## Backend

- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- PostgreSQL (Neon)

## Testing

- Pytest

---

# Project Goals

The primary goal of this project was to build a small but well-structured system that remains understandable and maintainable as it evolves.

Key engineering priorities:

- Clear architectural boundaries
- Enforced workflow rules
- Schema validation
- Safe interfaces
- Automated verification
- Observable state transitions
- AI-assisted but manually reviewed implementation

---

# Core Features

- Create tasks
- View tasks
- Workflow-based task transitions
- Controlled state management
- Audit history tracking
- Validation on frontend and backend
- Automated backend tests
- Real-time task refresh using polling

---

# Workflow System

Tasks move through controlled lifecycle states.

## Supported States

- TODO
- IN_PROGRESS
- IN_REVIEW
- DONE
- CANCELLED

## Allowed Transitions

```txt
TODO -> IN_PROGRESS
TODO -> CANCELLED

IN_PROGRESS -> IN_REVIEW
IN_PROGRESS -> CANCELLED

IN_REVIEW -> DONE
IN_REVIEW -> IN_PROGRESS
```
