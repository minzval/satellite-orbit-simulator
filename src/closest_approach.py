import numpy as np


def calculate_distance(position1, position2):
    """
    Calculate the Euclidean distance between two position vectors.
    """
    return np.linalg.norm(position1 - position2)


def find_closest_approach(result1, result2):
    """
    Find the closest approach between two propagated satellites.

    Parameters
    ----------
    result1 : dict
    result2 : dict

    Returns
    -------
    dict
    """

    positions1 = result1["positions"]
    positions2 = result2["positions"]

    minimum_distance = float("inf")
    minimum_index = 0

    total_steps = min(len(positions1), len(positions2))

    for i in range(total_steps):

        distance = calculate_distance(
            positions1[i],
            positions2[i]
        )

        if distance < minimum_distance:
            minimum_distance = distance
            minimum_index = i

    return {

        "satellite_1": result1["name"],
        "satellite_2": result2["name"],

        "minimum_distance": minimum_distance,

        "time": result1["times"][minimum_index],

        "index": minimum_index

    }