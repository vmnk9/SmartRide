import math

def distance(loc1, loc2):
    return ((loc1["lat"] - loc2["lat"])**2 + (loc1["lon"] - loc2["lon"])**2)**0.5

def find_closest_driver(ride, drivers):
    closest = None
    min_dist = float('inf')
    for driver_id, loc in drivers.items():
        d = distance({"lat": ride.lat, "lon": ride.lon}, loc)
        if d < min_dist:
            min_dist = d
            closest = {"driver_id": driver_id, "location": loc}
    return closest
