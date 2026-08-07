from src.closest_approach import find_closest_approach


def compare_target(target_result, all_results):
    """
    Compare one target satellite against all other
    propagated satellites.

    Returns results sorted by minimum distance.
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


def apply_risk_threshold(comparisons, threshold_km=5.0):
    """
    Flag closest approaches below the specified
    screening threshold.

    Parameters
    ----------
    comparisons : list
        Closest-approach results.

    threshold_km : float
        Distance threshold in kilometres.

    Returns
    -------
    list
        Updated comparison results.
    """

    for result in comparisons:

        result["threshold_km"] = threshold_km

        result["risk_flag"] = (
            result["minimum_distance"] < threshold_km
        )

    return comparisons