from dataclasses import dataclass
from typing import List


@dataclass
class SatelliteTLE:
    name: str
    line1: str
    line2: str


def load_tles(path: str) -> List[SatelliteTLE]:
    """
    Loads TLEs from a text file in the format:
    NAME
    line1
    line2
    (blank line optional)
    """
    satellites: List[SatelliteTLE] = []
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Every TLE set is 3 lines: name, line1, line2
    if len(lines) % 3 != 0:
        raise ValueError("TLE file format error: expected groups of 3 lines (name, line1, line2).")

    for i in range(0, len(lines), 3):
        name = lines[i]
        line1 = lines[i + 1]
        line2 = lines[i + 2]
        satellites.append(SatelliteTLE(name=name, line1=line1, line2=line2))

    return satellites

