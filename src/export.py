import csv
from pathlib import Path


def export_comparisons(
    comparisons,
    filename="closest_approaches.csv"
):
    """
    Export closest-approach results to a CSV file.
    """

    output_path = Path(filename)

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Satellite 1",
            "Satellite 2",
            "Minimum Distance (km)",
            "Time",
            "Threshold (km)",
            "Risk Flag"
        ])

        for result in comparisons:

            writer.writerow([
                result["satellite_1"],
                result["satellite_2"],
                f"{result['minimum_distance']:.3f}",
                result["time"].isoformat(),
                result["threshold_km"],
                "FLAG" if result["risk_flag"] else "CLEAR"
            ])

    print(f"Saved: {output_path}")