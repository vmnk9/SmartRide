from pydantic import BaseModel

class RideRequest(BaseModel):
    rider_id: str
    lat: float
    lon: float

class DriverLocation(BaseModel):
    driver_id: str
    lat: float
    lon: float
