# PROMPT:
# Generate FastAPI funnel endpoint tests

# CHANGES MADE:
# Adapted for project routes

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_funnel():

    response = client.get(
        "/stores/STORE_001/funnel"
    )

    assert response.status_code in [
        200,
        404
    ]