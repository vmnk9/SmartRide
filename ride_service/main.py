from fastapi import FastAPI, HTTPException
from ride_service.models import RideRequest, DriverLocation
from ride_service.matching import find_closest_driver
from ride_service.storage import db
app = FastAPI()

@app.post("/request_ride")
def request_ride(ride: RideRequest):
    driver = find_closest_driver(ride, db["drivers"])
    if not driver:
        raise HTTPException(status_code=404, detail="No drivers nearby")
    db["rides"].append({"rider": ride.dict(), "driver": driver})
    return {"assigned_driver": driver}

@app.post("/update_driver_location")
def update_driver_location(location: DriverLocation):
    db["drivers"][location.driver_id] = location.dict()
    return {"status": "updated"}
