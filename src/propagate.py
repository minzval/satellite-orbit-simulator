from datetime import datetime, timezone

import numpy as np
from sgp4.api import Satrec, jday

from src.tle_loader import load_tles


def propagate_once():
    """
    Load the first satellite from the TLE file and propagate
    its orbit to the current UTC time.
    """

    # Load satellites
    satellites = load_tles("data/sample_tles.txt")

    if not satellites:
        raise ValueError("No satellites found in the TLE file.")

    # Select the first satellite
    sat = satellites[0]

    # Build the SGP4 satellite object
    satrec = Satrec.twoline2rv(
        sat["line1"],
        sat["line2"]
    )

    # Current UTC time
    now = datetime.now(timezone.utc)

    jd, fr = jday(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second + now.microsecond / 1_000_000
    )

    # Propagate orbit
    error_code, position, velocity = satrec.sgp4(jd, fr)

    if error_code != 0:
        raise RuntimeError(f"SGP4 returned error code {error_code}")

    position = np.array(position)
    velocity = np.array(velocity)

    print(f"Satellite: {sat['name']}")
    print(f"UTC Time: {now.isoformat()}")
    print(f"Position (km): {position}")
    print(f"Velocity (km/s): {velocity}")


if __name__ == "__main__":
    propagate_once()