from pathlib import Path

import matplotlib.pyplot as plt


FIGURES_DIR = Path("figures")
FIGURES_DIR.mkdir(exist_ok=True)


EARTH_RADIUS_KM = 6378.137


def plot_xy(result):
    """
    Plot the satellite orbit in the equatorial XY plane.
    """

    positions = result["positions"]

    x = positions[:, 0]
    y = positions[:, 1]

    fig, ax = plt.subplots(figsize=(8, 8))

    # Satellite trajectory
    ax.plot(
        x,
        y,
        linewidth=1.5,
        label=result["name"]
    )

    # Earth
    earth = plt.Circle(
        (0, 0),
        EARTH_RADIUS_KM,
        alpha=0.35,
        label="Earth"
    )

    ax.add_patch(earth)

    # Mark the beginning and end of the propagated orbit
    ax.scatter(
        x[0],
        y[0],
        s=60,
        marker="o",
        label="Start"
    )

    ax.scatter(
        x[-1],
        y[-1],
        s=60,
        marker="x",
        label="End"
    )

    ax.set_title(
        f"Satellite Orbit — XY Projection\n"
        f"{result['name']}"
    )

    ax.set_xlabel("X Position (km)")
    ax.set_ylabel("Y Position (km)")

    ax.set_aspect("equal", adjustable="box")

    # Give the plot some space around the orbit
    max_distance = max(
        max(abs(x)),
        max(abs(y)),
        EARTH_RADIUS_KM
    )

    plot_limit = max_distance * 1.15

    ax.set_xlim(
        -plot_limit,
        plot_limit
    )

    ax.set_ylim(
        -plot_limit,
        plot_limit
    )

    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    output = FIGURES_DIR / "orbit_xy.png"

    fig.savefig(
        output,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

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

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.plot(
        elapsed_minutes,
        altitudes
    )

    ax.set_title(
        f"Altitude vs Time\n{result['name']}"
    )

    ax.set_xlabel(
        "Time Since Start (minutes)"
    )

    ax.set_ylabel(
        "Altitude (km)"
    )

    ax.grid(True)

    fig.tight_layout()

    output = FIGURES_DIR / "altitude_vs_time.png"

    fig.savefig(
        output,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"Saved: {output}")


def plot_distance(result1, result2):
    """
    Plot distance between two satellites over time.
    """

    positions1 = result1["positions"]
    positions2 = result2["positions"]

    times = result1["times"]

    distances = []

    for position1, position2 in zip(
        positions1,
        positions2
    ):

        dx = position1[0] - position2[0]
        dy = position1[1] - position2[1]
        dz = position1[2] - position2[2]

        distance = (
            dx ** 2
            + dy ** 2
            + dz ** 2
        ) ** 0.5

        distances.append(distance)

    elapsed_minutes = [
        (time - times[0]).total_seconds() / 60
        for time in times
    ]

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.plot(
        elapsed_minutes,
        distances
    )

    ax.set_title(
        f"Distance vs Time\n"
        f"{result1['name']} vs {result2['name']}"
    )

    ax.set_xlabel(
        "Time Since Start (minutes)"
    )

    ax.set_ylabel(
        "Distance (km)"
    )

    ax.grid(True)

    fig.tight_layout()

    output_name = (
        f"distance_"
        f"{result1['name'].replace(' ', '_')}_"
        f"{result2['name'].replace(' ', '_')}.png"
    )

    output = FIGURES_DIR / output_name

    fig.savefig(
        output,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"Saved: {output}")