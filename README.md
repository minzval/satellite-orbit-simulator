# Satellite Orbit Simulator

A Python-based satellite orbit analysis tool that uses Two-Line Element (TLE) data and the SGP4 propagation model to simulate satellite orbits, visualize trajectories, and analyze closest approaches between satellites.

## Project Overview

This project was developed to explore practical applications of orbital mechanics and scientific programming using Python.

The simulator takes satellite TLE data as input and uses the SGP4 model to calculate satellite positions and velocities over a selected period of time.

The resulting data is used to:

- Propagate satellite orbits
- Calculate satellite altitude
- Visualize orbital trajectories
- Compare multiple satellites
- Determine closest approaches
- Plot separation distance over time
- Apply a simple distance-based screening threshold
- Export analysis results to CSV

---

## Features

### TLE Data Handling

The program reads satellite information from a TLE file containing:

- Satellite name
- TLE line 1
- TLE line 2

Example satellites currently included in the sample dataset:

- ISS (ZARYA)
- HUBBLE SPACE TELESCOPE
- NOAA 15

### SGP4 Orbit Propagation

Satellite positions are calculated using the SGP4 propagation model through the Python `sgp4` library.

The simulator generates:

- Position vectors in kilometres
- Velocity vectors in kilometres per second
- Time-series position data
- Satellite altitude

### Orbit Visualization

The project generates an XY projection of the satellite orbit and an altitude-versus-time graph.

Generated figures are stored in:

```text
figures/
