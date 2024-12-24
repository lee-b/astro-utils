# astro-utils

These are some simple tools for digital astrophotography.

### obs-list.py: Natural Satellite Observation List Generator

This script generates a list of **Right Ascension (RA)** and **Declination (Dec)** coordinates, over time, for capturing multiple images of natural satellite (e.g., moons like Io and Europa). This allows you to take the photos, stack the images, and end up with a great shot, without worrying about what position a moon is in its orbit
around its planet at any given time, relative to your position on Earth.  It should also work for many other orbital bodies, as the underlying data is pulled from JPL's Horizons project.

## Requirements

- Python 3.x
- `astropy` library
- `astroquery` library

Install the required libraries using `pip`:

```bash
pip install astropy astroquery
```

## Usage

The script queries the **JPL Horizons** system to compute the **RA/Dec coordinates** of a target natural satellite (such as Ceres) at specified epochs. You provide the name of the target satellite, your observation location (longitude, latitude, and elevation), and the time intervals for the observation list.

Run the script with the following syntax:

```bash
python obs-list.py <object_name> <longitude> <latitude> <elevation>
```

### Example:

```bash
python obs-list.py Ceres -74.0466891 40.6892534 0.093
```

This will output the RA/Dec coordinates for `Ceres` at 60-second intervals, starting from the current time, as observed from the specified location (Longitude: -74.0466891, Latitude: 40.6892534, Elevation: 0.093 km).

### Example Output:

```
Epoch: 2024-Dec-24 19:24:00.889 RA: 310.258610° Dec: -25.552470°
Epoch: 2024-Dec-24 19:25:00.889 RA: 310.258890° Dec: -25.552400°
Epoch: 2024-Dec-24 19:26:00.889 RA: 310.259160° Dec: -25.552330°
Epoch: 2024-Dec-24 19:27:00.889 RA: 310.259430° Dec: -25.552270°
Epoch: 2024-Dec-24 19:28:00.889 RA: 310.259700° Dec: -25.552200°
Epoch: 2024-Dec-24 19:29:00.889 RA: 310.259970° Dec: -25.552140°
Epoch: 2024-Dec-24 19:30:00.889 RA: 310.260250° Dec: -25.552070°
Epoch: 2024-Dec-24 19:31:00.889 RA: 310.260520° Dec: -25.552000°
Epoch: 2024-Dec-24 19:32:00.889 RA: 310.260790° Dec: -25.551940°
Epoch: 2024-Dec-24 19:33:00.889 RA: 310.261060° Dec: -25.551870°
```

### How it Works

- The script takes in an object name (e.g., Ceres), an observer's location (longitude, latitude, elevation), and generates a series of epochs (timestamps).
- The **`astroquery`** package is used to query the **JPL Horizons** system for the RA/Dec coordinates of the specified object at each epoch.
- The RA/Dec values are printed out at each epoch, which can be used for pointing a telescope to capture images for stacking.

## Notes

- The epochs are generated starting from the current time and are spaced 60 seconds apart (you can adjust the interval and number of steps if needed).
- The RA/Dec values are provided in degrees, formatted to six decimal places for precision.
  
## License

This project is licensed under the GNU Affero GPL v3 License (only)

