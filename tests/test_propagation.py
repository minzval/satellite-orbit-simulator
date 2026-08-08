from datetime import datetime, timezone
from pathlib import Path

from src.tle_loader import load_tles
from src.propagate import propagate_satellite


PROJECT_ROOT = Path(__file__).resolve().parents[1]

TLE_FILE = PROJECT_ROOT / "data" / "sample_tles.txt"


def test_propagation():

    satellites = load_tles(
        str(TLE_FILE)
    )

    satellite = satellites[0]

    start_time = datetime(
        2026,
        8,
        7,
        12,
        0,
        0,
        tzinfo=timezone.utc
    )

    result = propagate_satellite(
        satellite,
        start_time=start_time,
        duration_minutes=10,
        step_minutes=1
    )

    assert result["name"] == satellite["name"]

    assert len(result["times"]) == 11

    assert result["positions"].shape == (
        11,
        3
    )

    assert result["velocities"].shape == (
        11,
        3
    )

    assert len(result["altitudes"]) == 11