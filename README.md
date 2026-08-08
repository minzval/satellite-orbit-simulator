# Satellite Orbit Simulator

A Python-based satellite orbit analysis tool that uses Two-Line Element (TLE) data and the SGP4 propagation model to simulate satellite motion, visualize orbits, and identify the closest approaches between multiple satellites.

## Project Overview

The project was developed to explore practical applications of orbital mechanics, satellite tracking, and scientific programming.

The program takes satellite TLE data as input and:

- Loads and validates satellite TLE data
- Propagates satellite positions using the SGP4 model
- Generates time-series orbital data
- Calculates satellite altitude
- Produces orbit visualizations
- Compares multiple satellites
- Identifies their closest approaches
- Records the time of closest approach
- Applies a simple distance-based risk classification
- Exports closest-approach results to CSV
- Includes automated tests for core functionality

## Technologies

- Python 3.10
- NumPy
- Matplotlib
- Pandas
- SGP4
- Pytest
- Git / GitHub

## Project Structure

```text
satellites-orbit-simulator/
│
├── data/
│   └── sample_tles.txt
│
├── figures/
│   ├── orbit_xy.png
│   └── altitude_vs_time.png
│
├── src/
│   ├── __init__.py
│   ├── tle_loader.py
│   ├── utils.py
│   ├── propagate.py
│   ├── plots.py
│   ├── closest_approach.py
│   ├── comparison.py
│   ├── export.py
│   └── main.py
│
├── tests/
│   ├── test_closest_approach.py
│   ├── test_tle_loader.py
│   └── test_propagation.py
│
├── closest_approaches.csv
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
