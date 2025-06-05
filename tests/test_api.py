from fastapi.testclient import TestClient
from ride_service.main import app

client = TestClient(app)

def test_update_driver_location_and_request_ride():
    # Update driver location
    response = client.post("/update_driver_location", json={
        "driver_id": "driver_123",
        "lat": 1.0,
        "lon": 2.0
    })
    assert response.status_code == 200
    assert response.json()["status"] == "updated"

    # Request a ride
    response = client.post("/request_ride", json={
        "rider_id": "rider_abc",
        "lat": 1.1,
        "lon": 2.1
    })
    assert response.status_code == 200
    data = response.json()
    assert "assigned_driver" in data
    assert data["assigned_driver"]["driver_id"] == "driver_123"
