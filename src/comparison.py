from src.closest_approach import find_closest_approach


def compare_target(
    target_result,
    all_results
):
    """
    Compare one target satellite against all other
    propagated satellites.

    Parameters
    ----------
    target_result : dict
        Propagation result for the target satellite.

    all_results : dict
        Dictionary containing propagation results
        for all satellites.

    Returns
    -------
    list of dict
        Closest-approach results sorted by distance.
    """

    comparisons = []

    for name, result in all_results.items():

        if name == target_result["name"]:
            continue

        closest = find_closest_approach(
            target_result,
            result
        )

        comparisons.append(closest)

    comparisons.sort(
        key=lambda result: result["minimum_distance"]
    )

    return comparisons