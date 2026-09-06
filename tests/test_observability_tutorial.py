from fastapi.testclient import TestClient

from docs_src.observability.tutorial002_py310 import app

client = TestClient(app)


def test_health_endpoint_returns_200():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_endpoint_returns_ok_status():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}


def test_logging_app_starts():
    """Verify the logging tutorial app can be imported and started without errors."""
    from docs_src.observability.tutorial001_py310 import app as logging_app

    logging_client = TestClient(logging_app)
    response = logging_client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Item 1"}
