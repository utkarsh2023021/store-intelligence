# PROMPT:
# Generate FastAPI health endpoint tests

# CHANGES MADE:
# Added project-specific assertions

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():

    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    data = response.json()

    assert "status" in data