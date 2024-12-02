from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_frames():
    response = client.get("/get_frames?depth_min=5&depth_max=10")
    assert response.status_code == 200
