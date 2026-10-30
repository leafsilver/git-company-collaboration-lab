from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_existing_task_summary() -> None:
    response = client.get("/tasks/1/summary")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Prepare release notes",
        "status": "in_progress",
        "summary": "Prepare release notes [in_progress]",
    }


def test_get_missing_task_summary() -> None:
    response = client.get("/tasks/999/summary")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}
