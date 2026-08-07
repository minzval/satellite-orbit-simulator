from datetime import datetime, timedelta, timezone

import numpy as np
from sgp4.api import Satrec

from src.tle_loader import load_tles
from src.utils import datetime_to_julian


def propagate_satellite(
    satellite,
    start_time=None,
    duration_minutes=90,
    step_minutes=1
):
    """
    Propagate one satellite over a fixed time interval.

    Parameters
    ----------
    satellite : dict
        Satellite containing name, line1 and line2.

    start_time : datetime, optional
        UTC starting time. If omitted, current UTC time is used.

    duration_minutes : int
        Total propagation duration.

    step_minutes : int
        Time interval between propagation points.

    Returns
    -------
    dict
        Propagation data including times, positions,
        velocities and altitudes.
    """

    if start_time is None:
        start_time = datetime.now(timezone.utc)

    if start_time.tzinfo is None:
        raise ValueError("start_time must be timezone-aware.")

    satrec = Satrec.twoline2rv(
        satellite["line1"],
        satellite["line2"]
    )

    times = []
    positions = []
    velocities = []
    altitudes = []

    earth_radius = 6378.137

    number_of_steps = duration_minutes // step_minutes + 1

    for step in range(number_of_steps):

        current_time = start_time + timedelta(
            minutes=step * step_minutes
        )

        jd, fr = datetime_to_julian(current_time)

        error, position, velocity = satrec.sgp4(jd, fr)

        if error != 0:
            raise RuntimeError(
                f"SGP4 error code {error} for "
                f"{satellite['name']}"
            )

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


def propagate_all(
    satellites,
    start_time=None,
    duration_minutes=90,
    step_minutes=1
):
    """
    Propagate multiple satellites using exactly the same
    time grid.

    Returns
    -------
    dict
        Satellite name -> propagation result.
    """

    if start_time is None:
        start_time = datetime.now(timezone.utc)

    results = {}

    for satellite in satellites:

        results[satellite["name"]] = propagate_satellite(
            satellite,
            start_time=start_time,
            duration_minutes=duration_minutes,
            step_minutes=step_minutes
        )

    return results


def main():

    satellites = load_tles("data/sample_tles.txt")

    results = propagate_all(satellites)

    print("\nPropagation Summary")
    print("-" * 60)

    for name, result in results.items():

        print(
            f"{name:<30}"
            f"{len(result['times']):>4} points   "
            f"Average altitude: "
            f"{result['altitudes'].mean():.2f} km"
        )


if __name__ == "__main__":
    main()