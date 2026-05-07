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

Invalid transitions are rejected by the backend service layer.

Examples:

- DONE -> TODO ❌
- TODO -> DONE ❌
- CANCELLED -> IN_PROGRESS ❌

---

# Architecture

The application follows a layered architecture to separate responsibilities and reduce coupling.

## Backend Flow

```txt
Route -> Schema -> Service -> Repository -> Database
```

## Layer Responsibilities

### Routes

- Request handling
- Response formatting
- Validation integration

### Schemas

- Request validation
- Input safety

### Services

- Business logic
- Workflow enforcement
- State transition rules

### Repositories

- Database interaction only

### Domain Layer

- Centralized workflow rules
- Allowed transitions

---

# Frontend Structure

```txt
src/
├── api/
├── components/
├── features/
│   └── tasks/
├── hooks/
├── layouts/
├── pages/
├── schemas/
├── types/
└── lib/
```

---

# Backend Structure

```txt
backend/
├── app/
│   ├── api/
│   ├── domain/
│   ├── extensions/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── tests/
```

---

# Validation Strategy

Validation is implemented at multiple layers.

## Frontend

- Zod schema validation
- Typed API interactions

## Backend

- Marshmallow request validation
- Workflow rule enforcement
- Invalid transition prevention

This prevents invalid states from entering the system.

---

# Database Design

## tasks

Stores task metadata and workflow state.

## task_history

Stores transition history for auditability and observability.

Each workflow transition creates a history entry.

---

# Testing

Backend tests were implemented using Pytest.

Covered scenarios:

- Task creation
- Invalid payload rejection
- Task retrieval
- Valid workflow transitions
- Invalid workflow transitions

Run tests:

```bash
pytest
```

---

# Setup Instructions

## Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`:

```env
DATABASE_URL=YOUR_DATABASE_URL
SECRET_KEY=supersecretkey
FLASK_ENV=development
```

Run migrations:

```bash
export FLASK_APP=run.py

flask db upgrade
```

Start backend:

```bash
python run.py
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# Engineering Tradeoffs

## Polling Instead of WebSockets

React Query polling was used for simplicity and maintainability instead of introducing websocket complexity.

## PostgreSQL Instead of SQLite

PostgreSQL was chosen to better represent relational persistence and migration workflows.

## Small Scope Over Feature Breadth

The project intentionally prioritizes correctness, architecture, and maintainability over large feature sets.

## No Authentication Layer

Authentication was intentionally excluded to keep the assessment focused on workflow correctness and system design.

---

# AI Usage Summary

AI assistance was used to accelerate implementation, scaffolding, and architectural iteration.

Generated code was manually reviewed and validated before integration.

Key safeguards used during development:

- Business logic centralized in services
- Workflow rules isolated in domain layer
- Validation enforced on both frontend and backend
- Repository layer restricted to persistence concerns
- Automated tests used to verify behavior after changes

AI-generated output was treated as a starting point rather than accepted without review.

---

# Future Improvements

Potential future enhancements:

- Authentication and authorization
- Role-based workflows
- Task comments
- Filtering and search
- Pagination
- Optimistic updates
- WebSocket-based realtime updates
- Deployment pipeline
- CI/CD automation

---

# Assessment Focus

This project intentionally prioritizes:

- simplicity
- maintainability
- predictable behavior
- safe state transitions
- clear architectural boundaries
- automated verification

over feature quantity or UI complexity.
