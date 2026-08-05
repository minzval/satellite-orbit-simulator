import numpy as np


def distance_between(position1, position2):
    """
    Calculate the Euclidean distance between two satellites.

    Parameters
    ----------
    position1 : ndarray
    position2 : ndarray

    Returns
    -------
    float
        Distance in kilometres.
    """

    return np.linalg.norm(position1 - position2)


def closest_approach(result1, result2):
    """
    Determine the closest approach between two propagated satellites.

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
    minimum_index = -1

    for i in range(min(len(positions1), len(positions2))):

        distance = distance_between(
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

        "time":

            result1["times"][minimum_index]

    }
