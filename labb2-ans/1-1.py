# En grundläggande matematisk funktion
def fuel_consumption(mass):
    return 1.5 * mass + 500


# Fråga och kovertera massans
input_mass = float(input("Ange lastens massa: "))

# Printa konsumtion med en avrundning till 2 decimaler flyttal
print(f"Förbrukning: {fuel_consumption(input_mass):.2f}")
