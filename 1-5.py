# Fråga efter hastigheten
speed_kmh = float(input("Ange hastigheten i km/tim: "))
speed_ms = speed_kmh / 3.6  # 60^2 / 1000 är konverteringsfaktorn mellan km/h och m/s

# Fråga efter bromsacceleration
a_b = float(input("Ange bromsacc. i m/s: "))

# Utför beräkningen
s_b = speed_ms**2 / (2 * a_b)

# Skriv ut resultatet
print(f"Bromssträckan är: {s_b} m")
