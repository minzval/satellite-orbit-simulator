from pathlib import Path

import matplotlib.pyplot as plt


FIGURES_DIR = Path("figures")
FIGURES_DIR.mkdir(exist_ok=True)


def plot_xy(result):
    """
    Plot X vs Y orbit projection.
    """

    positions = result["positions"]

    x = positions[:, 0]
    y = positions[:, 1]

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, linewidth=1.5)

    plt.scatter(0, 0, s=120, label="Earth")

    plt.title(f"Orbit Projection\n{result['name']}")
    plt.xlabel("X Position (km)")
    plt.ylabel("Y Position (km)")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()

    output = FIGURES_DIR / "orbit_xy.png"
    plt.savefig(output, dpi=300)
    plt.close()

    print(f"Saved: {output}")


def plot_altitude(result):
    """
    Plot altitude over time.
    """

    altitudes = result["altitudes"]
    times = range(len(altitudes))

    plt.figure(figsize=(10, 5))
    plt.plot(times, altitudes)

    plt.title(f"Altitude vs Time\n{result['name']}")
    plt.xlabel("Time Step")
    plt.ylabel("Altitude (km)")
    plt.grid(True)

    output = FIGURES_DIR / "altitude_vs_time.png"
    plt.savefig(output, dpi=300)
    plt.close()

    print(f"Saved: {output}")
