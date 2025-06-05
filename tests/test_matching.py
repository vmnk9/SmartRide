from ride_service.matching import find_closest_driver
from ride_service.models import RideRequest

def test_basic_matching():
    drivers = {
        "d1": {"lat": 1.0, "lon": 1.0},
        "d2": {"lat": 5.0, "lon": 5.0}
    }
    ride = RideRequest(rider_id="r1", lat=1.2, lon=1.1)
    driver = find_closest_driver(ride, drivers)
    assert driver["driver_id"] == "d1"
