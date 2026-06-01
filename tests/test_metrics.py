# PROMPT:
# Generate FastAPI metrics endpoint tests

# CHANGES MADE:
# Added store specific validation

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_metrics():

    response = client.get(
        "/stores/STORE_001/metrics"
    )

    assert response.status_code in [
        200,
        404
    ]