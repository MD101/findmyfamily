from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_location():
    response = client.post("/post_location", json={"latitude": 40.7128, "longitude": -74.0060, "timestamp": 1640995200000, "accuracy": 10.5, "device_id": "1234567890"})
    assert response.status_code == 200
    assert response.json() == {"Message": "Location received"}