#!/usr/bin/env python3

import datetime
import sys
import astropy.units as u
from astroquery.jplhorizons import Horizons
from astropy.time import Time

# Input from command-line
obj = sys.argv[1]
lon = float(sys.argv[2])
lat = float(sys.argv[3])
elev = float(sys.argv[4])

# Observer's location
observer_loc = {
    'lon': lon * u.deg,
    'lat': lat * u.deg,
    'elevation': elev * u.km
}

# Setup the time range and epochs
start = datetime.datetime.now()
step_delta = datetime.timedelta(seconds=60)
num_steps = 10

epochs = [Time(start + i * step_delta).jd for i in range(num_steps)]

# Use Horizons to query the object at the specified epochs
obj = Horizons(id=obj, location=observer_loc, epochs=epochs)

# Query for RA/Dec values
ephs = obj.ephemerides()

# Print RA/Dec for each epoch
for epoch_data in ephs:
    ra = epoch_data['RA']
    dec = epoch_data['DEC']
    time_str = epoch_data['datetime_str']
    print(f"Epoch: {time_str} RA: {ra:.6f}° Dec: {dec:.6f}°")

