from pathlib import Path

from src.tle_loader import load_tles


PROJECT_ROOT = Path(__file__).resolve().parents[1]

TLE_FILE = PROJECT_ROOT / "data" / "sample_tles.txt"


def test_load_tles():

    satellites = load_tles(
        str(TLE_FILE)
    )

    assert len(satellites) >= 2

    for satellite in satellites:

        assert "name" in satellite
        assert "line1" in satellite
        assert "line2" in satellite

        assert satellite["name"]
        assert satellite["line1"].startswith("1 ")
        assert satellite["line2"].startswith("2 ")