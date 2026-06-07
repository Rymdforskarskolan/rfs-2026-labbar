# Bromssträcka (bonus: ange bromsacceleration i g)
# Detta är ett bonusexempel för fråga 1-12 där man anger bromsacceleration
# i enheter av g (multipel av 9.81 m/s^2)

speed_kmh = float(input("Ange hastigheten i km/tim: "))
speed_ms = speed_kmh / 3.6

brake_g = float(input("Ange bromsacc. i g: "))
braking_acceleration = 9.81 * brake_g

braking_distance = speed_ms**2 / (2 * braking_acceleration)

print(f"Bromssträckan är: {braking_distance} m")
