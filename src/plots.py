from pathlib import Path

import matplotlib.pyplot as plt


FIGURES_DIR = Path("figures")
FIGURES_DIR.mkdir(exist_ok=True)


def plot_xy(result):
    """
    Plot X vs Y projection of a satellite orbit.
    """

    positions = result["positions"]

    x = positions[:, 0]
    y = positions[:, 1]

    plt.figure(figsize=(8, 8))

    plt.plot(x, y, linewidth=1.5)

    plt.scatter(
        0,
        0,
        s=120,
        label="Earth"
    )

    plt.title(
        f"Orbit Projection\n{result['name']}"
    )

    plt.xlabel("X Position (km)")
    plt.ylabel("Y Position (km)")

    plt.axis("equal")
    plt.grid(True)
    plt.legend()

    output = FIGURES_DIR / "orbit_xy.png"

    plt.savefig(
        output,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Saved: {output}")


def plot_altitude(result):
    """
    Plot satellite altitude against time.
    """

    altitudes = result["altitudes"]
    times = result["times"]

    elapsed_minutes = [
        (time - times[0]).total_seconds() / 60
        for time in times
    ]

    plt.figure(figsize=(10, 5))

    plt.plot(
        elapsed_minutes,
        altitudes
    )

    plt.title(
        f"Altitude vs Time\n{result['name']}"
    )

    plt.xlabel("Time Since Start (minutes)")
    plt.ylabel("Altitude (km)")

    plt.grid(True)

    output = FIGURES_DIR / "altitude_vs_time.png"

    plt.savefig(
        output,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Saved: {output}")


def plot_distance(result1, result2):
    """
    Plot the distance between two satellites over time.
    """

    positions1 = result1["positions"]
    positions2 = result2["positions"]

    times = result1["times"]

    distances = []

    for position1, position2 in zip(
        positions1,
        positions2
    ):
        distance = (
            (position1[0] - position2[0]) ** 2
            + (position1[1] - position2[1]) ** 2
            + (position1[2] - position2[2]) ** 2
        ) ** 0.5

        distances.append(distance)

    elapsed_minutes = [
        (time - times[0]).total_seconds() / 60
        for time in times
    ]

    plt.figure(figsize=(10, 5))

    plt.plot(
        elapsed_minutes,
        distances
    )

    plt.title(
        f"Distance vs Time\n"
        f"{result1['name']} vs {result2['name']}"
    )

    plt.xlabel("Time Since Start (minutes)")
    plt.ylabel("Distance (km)")

    plt.grid(True)

    output_name = (
        f"distance_"
        f"{result1['name'].replace(' ', '_')}_"
        f"{result2['name'].replace(' ', '_')}.png"
    )

    output = FIGURES_DIR / output_name

    plt.savefig(
        output,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Saved: {output}")