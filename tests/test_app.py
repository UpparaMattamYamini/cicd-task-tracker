
from app import app


def test_home_page():
    # Check that the home page opens successfully.
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"My First CI/CD Project" in response.data


def test_health_endpoint():
    # Check that the health endpoint reports a healthy application.
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_tasks_endpoint():
    # Check that the tasks endpoint returns an empty list.
    client = app.test_client()
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.get_json() == []
