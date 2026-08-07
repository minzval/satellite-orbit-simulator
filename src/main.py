from datetime import datetime, timezone

from src.tle_loader import load_tles
from src.propagate import propagate_all
from src.plots import plot_xy, plot_altitude
from src.comparison import compare_target


def main():

    satellites = load_tles("data/sample_tles.txt")

    if len(satellites) < 2:
        raise ValueError(
            "At least two satellites are required."
        )

    # One common starting time for every satellite
    start_time = datetime.now(timezone.utc)

    # Propagate every satellite using the same time grid
    results = propagate_all(
        satellites,
        start_time=start_time,
        duration_minutes=90,
        step_minutes=1
    )

    # Target satellite
    target_name = satellites[0]["name"]

    target_result = results[target_name]

    # Create plots for target satellite
    plot_xy(target_result)
    plot_altitude(target_result)

    # Compare target against every other satellite
    comparisons = compare_target(
        target_result,
        results
    )

    print("\nClosest Approaches")
    print("-" * 60)

    for comparison in comparisons:

        print(
            f"{comparison['satellite_2']:<30}"
            f"{comparison['minimum_distance']:10.2f} km"
        )

        print(
            f"{'':30}"
            f"Time: {comparison['time']}"
        )

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()