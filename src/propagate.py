from src.plots import plot_xy, plot_altitude
from datetime import datetime, timedelta, timezone

import numpy as np
from sgp4.api import Satrec

from src.tle_loader import load_tles
from src.utils import datetime_to_julian


def propagate_satellite(
    satellite,
    duration_minutes=90,
    step_minutes=1
):
    """
    Propagate one satellite over a period of time.

    Returns a dictionary containing all orbit data.
    """

    satrec = Satrec.twoline2rv(
        satellite["line1"],
        satellite["line2"]
    )

    start_time = datetime.now(timezone.utc)

    times = []
    positions = []
    velocities = []
    altitudes = []

    earth_radius = 6378.137

    steps = duration_minutes // step_minutes + 1

    for step in range(steps):

        current_time = start_time + timedelta(
            minutes=step * step_minutes
        )

        jd, fr = datetime_to_julian(current_time)

        error, position, velocity = satrec.sgp4(jd, fr)

        if error != 0:
            continue

        position = np.array(position)
        velocity = np.array(velocity)

        radius = np.linalg.norm(position)
        altitude = radius - earth_radius

        times.append(current_time)
        positions.append(position)
        velocities.append(velocity)
        altitudes.append(altitude)

    return {
        "name": satellite["name"],
        "times": times,
        "positions": np.array(positions),
        "velocities": np.array(velocities),
        "altitudes": np.array(altitudes),
    }


def main():

    satellites = load_tles("data/sample_tles.txt")

    satellite = satellites[0]

    result = propagate_satellite(satellite)

    print(f"\nSatellite: {result['name']}")
    print(f"Generated {len(result['times'])} orbit points.")
    print(f"Average altitude: {result['altitudes'].mean():.2f} km")

    plot_xy(result)
    plot_altitude(result)

    print("\nOrbit plots created successfully.")


if __name__ == "__main__":
    main()