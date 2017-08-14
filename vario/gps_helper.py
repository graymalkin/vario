from math import radians, cos, sin, asin, sqrt

def minutes_to_decimal(coord):
    if len(coord) < len("DDMMMmmmE"):
        raise ValueError("Input too short for a valid GPS coordinate")

    # get seconds
    mmm = float(coord[-4:-1]) / 100.0

    # get minutes
    MMM = float(coord[-7:-4])

    # get degrees
    DD = float(coord[0:-7])

    val = DD + (MMM / 60.0) + (mmm / 3600.0)
    if coord[-1] == 'W' or coord[-1] == 'S':
        val = -val
    return val


# https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
