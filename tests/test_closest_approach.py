import numpy as np

from src.closest_approach import (
    calculate_distance,
    find_closest_approach
)


def test_calculate_distance():

    position1 = np.array([0.0, 0.0, 0.0])
    position2 = np.array([3.0, 4.0, 0.0])

    distance = calculate_distance(
        position1,
        position2
    )

    assert distance == 5.0


def test_find_closest_approach():

    result1 = {
        "name": "Satellite A",
        "times": [0, 1, 2],
        "positions": np.array([
            [0.0, 0.0, 0.0],
            [10.0, 0.0, 0.0],
            [20.0, 0.0, 0.0]
        ])
    }

    result2 = {
        "name": "Satellite B",
        "times": [0, 1, 2],
        "positions": np.array([
            [5.0, 0.0, 0.0],
            [11.0, 0.0, 0.0],
            [30.0, 0.0, 0.0]
        ])
    }

    result = find_closest_approach(
        result1,
        result2
    )

    assert result["minimum_distance"] == 1.0
    assert result["time"] == 1