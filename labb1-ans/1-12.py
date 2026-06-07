# Bromssträcka (facitfråga)
# Programmet läser hastighet i km/h och bromsacceleration i m/s^2
# och beräknar bromssträckan enligt s = v^2 / (2 a)

speed_kmh = float(input("Ange hastigheten i km/tim: "))
# Konvertera km/h -> m/s
speed_ms = speed_kmh / 3.6

# Läs in bromsacceleration (i m/s^2)
braking_acceleration = float(input("Ange bromsacceleration i m/s^2: "))

# Beräkna bromssträcka
braking_distance = speed_ms**2 / (2 * braking_acceleration)

# Skriv ut avrundat till 3 decimaler (nyckeln enligt uppgiften)
print(f"Bromssträckan är: {braking_distance:.3f} m")
