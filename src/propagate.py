from datetime import datetime, timezone

import numpy as np
from sgp4.api import Satrec, jday

from src.tle_loader import load_tles


def propagate_once():
    # Load one satellite from your TLE file
    sats = load_tles("data/sample_tles.txt")
    sat = sats[0]

    # Build SGP4 satellite object
    satrec = Satrec.twoline2rv(sat.line1, sat.line2)

    # Use "now" in UTC
    now = datetime.now(timezone.utc)
    jd, fr = jday(now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Propagate
    e, r, v = satrec.sgp4(jd, fr)  # r in km, v in km/s

    if e != 0:
        raise RuntimeError(f"SGP4 error code: {e}")

    r = np.array(r)
    v = np.array(v)

    print(f"Satellite: {sat.name}")
    print(f"UTC time:  {now.isoformat()}")
    print(f"Position (km): {r}")
    print(f"Velocity (km/s): {v}")


if __name__ == "__main__":
    propagate_once()
