"""
tle_loader.py

Functions for loading Two-Line Element (TLE) satellite data from a text file.

Each satellite is represented by three lines:

Satellite Name
TLE Line 1
TLE Line 2
"""

from pathlib import Path
from typing import Dict, List


def load_tles(file_path: str) -> List[Dict[str, str]]:
    """
    Load satellites from a TLE file.

    Parameters
    ----------
    file_path : str
        Path to the TLE text file.

    Returns
    -------
    list of dict
        Each dictionary contains:
            name
            line1
            line2
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"TLE file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    if len(lines) % 3 != 0:
        raise ValueError(
            "Invalid TLE file. Every satellite must contain exactly three lines."
        )

    satellites = []

    for i in range(0, len(lines), 3):

        name = lines[i]
        line1 = lines[i + 1]
        line2 = lines[i + 2]

        if not line1.startswith("1 "):
            raise ValueError(
                f"Invalid first TLE line for satellite '{name}'."
            )

        if not line2.startswith("2 "):
            raise ValueError(
                f"Invalid second TLE line for satellite '{name}'."
            )

        satellites.append(
            {
                "name": name,
                "line1": line1,
                "line2": line2,
            }
        )

    return satellites


def print_satellites(satellites: List[Dict[str, str]]) -> None:
    """
    Print all loaded satellites.
    """

    print(f"\nLoaded {len(satellites)} satellites:\n")

    for i, satellite in enumerate(satellites, start=1):
        print(f"{i}. {satellite['name']}")


if __name__ == "__main__":

    satellites = load_tles("../data/sample_tles.txt")

    print_satellites(satellites)