"""Tests for main.py FastAPI endpoints."""

import pytest


class TestGetTasks:
    """Tests for GET /tasks endpoint."""

    def test_get_tasks_returns_list(self, client):
        """Test that /tasks returns a list of tasks."""
        response = client.get("/tasks")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_get_tasks_returns_two_tasks(self, client):
        """Test that /tasks returns exactly 2 tasks."""
        response = client.get("/tasks")
        data = response.json()
        assert len(data) == 2

    def test_get_tasks_structure(self, client):
        """Test that each task has id and task fields."""
        response = client.get("/tasks")
        data = response.json()
        for task in data:
            assert "id" in task
            assert "task" in task

    def test_get_tasks_content(self, client):
        """Test the actual content of returned tasks."""
        response = client.get("/tasks")
        data = response.json()
        assert data[0] == {"id": 1, "task": "Task 1 completed"}
        assert data[1] == {"id": 2, "task": "Task 2 completed"}


class TestGetTaskById:
    """Tests for GET /tasks/{task_id} endpoint."""

    def test_get_task_default_id(self, client):
        """Test getting a task with default id (1)."""
        response = client.get("/tasks/1")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1

    def test_get_task_without_details(self, client):
        """Test getting a task without include_details flag."""
        response = client.get("/tasks/5")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 5
        assert "details" not in data
        assert "FALSE" in data["task"]

    def test_get_task_with_details_true(self, client):
        """Test getting a task with include_details=true."""
        response = client.get("/tasks/3?include_details=true")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 3
        assert "details" in data
        assert "TRUE" in data["task"]

    def test_get_task_with_details_false(self, client):
        """Test getting a task with include_details=false."""
        response = client.get("/tasks/2?include_details=false")
        assert response.status_code == 200
        data = response.json()
        assert "details" not in data

    def test_get_task_invalid_id_zero(self, client):
        """Test getting a task with invalid id (0)."""
        response = client.get("/tasks/0")
        assert response.status_code == 200
        data = response.json()
        assert "error" in data
        assert "Invalid task ID" in data["error"]

    def test_get_task_invalid_id_negative(self, client):
        """Test getting a task with negative id."""
        response = client.get("/tasks/-1")
        assert response.status_code == 200
        data = response.json()
        assert "error" in data

    @pytest.mark.parametrize("task_id", [1, 2, 5, 10, 100])
    def test_get_task_various_valid_ids(self, client, task_id):
        """Test getting tasks with various valid IDs."""
        response = client.get(f"/tasks/{task_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id
