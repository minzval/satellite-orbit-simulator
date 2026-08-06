from src.propagate import propagate_satellite


def propagate_all(satellites):
    """
    Propagate every satellite in the supplied list.

    Returns
    -------
    dict
        {
            satellite_name: propagation_result
        }
    """

    results = {}

    for satellite in satellites:
        result = propagate_satellite(satellite)
        results[result["name"]] = result

    return results