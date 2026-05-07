# Fråga efter hastigheten
speed_kmh = float(input("Ange hastigheten i km/tim: "))
speed_ms = speed_kmh / 3.6  # 60^2 / 1000 är konverteringsfaktorn mellan km/h och m/s

# Fråga efter bromsacceleration
brake_g = float(input("Ange bromsacc. i g: "))

# Beräkna a_b som multipel av 9.81 m/s^2
a_b = 9.81 * brake_g

# Utför beräkningen
s_b = speed_ms**2 / (2 * a_b)

# Skriv ut resultatet
print(f"Bromssträckan är: {s_b} m")
