def test_create_task(client):
    response = client.post(
        "/api/tasks",
        json={
            "title": "Test Task",
            "description": "Testing task creation",
            "priority": "HIGH",
        },
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Test Task"
    assert data["status"] == "TODO"
    assert data["priority"] == "HIGH"


def test_create_task_invalid_payload(client):
    response = client.post(
        "/api/tasks",
        json={
            "title": "",
            "priority": "INVALID",
        },
    )

    assert response.status_code == 400


def test_get_tasks(client):
    client.post(
        "/api/tasks",
        json={
            "title": "Task One",
            "priority": "LOW",
        },
    )

    response = client.get("/api/tasks")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) >= 1


def test_valid_transition(client):
    create_response = client.post(
        "/api/tasks",
        json={
            "title": "Transition Test",
            "priority": "MEDIUM",
        },
    )

    task = create_response.get_json()

    response = client.post(
        f"/api/tasks/{task['id']}/transition",
        json={
            "to_status": "IN_PROGRESS",
        },
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "IN_PROGRESS"


def test_invalid_transition(client):
    create_response = client.post(
        "/api/tasks",
        json={
            "title": "Invalid Transition",
            "priority": "HIGH",
        },
    )

    task = create_response.get_json()

    response = client.post(
        f"/api/tasks/{task['id']}/transition",
        json={
            "to_status": "DONE",
        },
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "Cannot transition" in data["error"]