from datetime import datetime, timezone

from src.tle_loader import load_tles
from src.propagate import propagate_all
from src.plots import (
    plot_xy,
    plot_altitude,
    plot_distance
)
from src.comparison import (
    compare_target,
    apply_risk_threshold
)
from src.export import export_comparisons


# --------------------------------------------------
# Configuration
# --------------------------------------------------

TARGET_SATELLITE = "ISS (ZARYA)"

RISK_THRESHOLD_KM = 5.0

PROPAGATION_DURATION_MINUTES = 90

PROPAGATION_STEP_MINUTES = 1


# --------------------------------------------------
# Main program
# --------------------------------------------------

def main():

    # Load TLE data
    satellites = load_tles(
        "data/sample_tles.txt"
    )

    if len(satellites) < 2:
        raise ValueError(
            "At least two satellites are required."
        )

    # Find target satellite
    satellite_names = [
        satellite["name"]
        for satellite in satellites
    ]

    if TARGET_SATELLITE not in satellite_names:

        raise ValueError(
            f"Target satellite '{TARGET_SATELLITE}' "
            f"was not found.\n"
            f"Available satellites: "
            f"{', '.join(satellite_names)}"
        )

    # One common starting time for all satellites
    start_time = datetime.now(timezone.utc)

    # Propagate all satellites
    results = propagate_all(
        satellites,
        start_time=start_time,
        duration_minutes=PROPAGATION_DURATION_MINUTES,
        step_minutes=PROPAGATION_STEP_MINUTES
    )

    # Get target propagation result
    target_result = results[TARGET_SATELLITE]

    # Generate target satellite plots
    plot_xy(target_result)

    plot_altitude(target_result)

    # Compare target against every other satellite
    comparisons = compare_target(
        target_result,
        results
    )

    # Apply risk screening threshold
    comparisons = apply_risk_threshold(
        comparisons,
        threshold_km=RISK_THRESHOLD_KM
    )

    # Display results
    print()
    print("Satellite Orbit Analysis")
    print("=" * 70)

    print(f"Target satellite: {TARGET_SATELLITE}")

    print(
        f"Propagation duration: "
        f"{PROPAGATION_DURATION_MINUTES} minutes"
    )

    print(
        f"Time step: "
        f"{PROPAGATION_STEP_MINUTES} minute(s)"
    )

    print(
        f"Risk screening threshold: "
        f"{RISK_THRESHOLD_KM:.1f} km"
    )

    print()
    print("Closest Approaches")
    print("-" * 70)

    for comparison in comparisons:

        satellite_name = comparison["satellite_2"]

        distance = comparison["minimum_distance"]

        flag = (
            "FLAG"
            if comparison["risk_flag"]
            else "CLEAR"
        )

        print(
            f"{satellite_name:<30}"
            f"{distance:10.2f} km   "
            f"{flag}"
        )

        print(
            f"{'':30}"
            f"Time: {comparison['time']}"
        )

        # Generate distance graph
        other_result = results[satellite_name]

        plot_distance(
            target_result,
            other_result
        )

    # Export CSV
    export_comparisons(
        comparisons
    )

    print()
    print("Analysis completed successfully.")


if __name__ == "__main__":
    main()