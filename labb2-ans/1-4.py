import math

EARTH_RADIUS = 6371e3  # m
G = 6.6743e-11  # Gravitationskonstanten
EARTH_MASS = 5.9722e24  # kg


def orbital_period(altitude):
    """Return orbital period in s for altitude w.r.t. earth surface in m"""
    return 2 * math.pi * math.sqrt((altitude + EARTH_RADIUS) ** 3 / (G * EARTH_MASS))


for i in range(6):
    alt = float(input(f"Ange höjd över ytan för sattelit {i + 1}: "))
    print(f"Omloppstid är {orbital_period(alt)}")
