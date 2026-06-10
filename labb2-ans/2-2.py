# En grundläggande matematisk funktion
def fuel_consumption(mass):
    return 1.5 * mass + 500


cargoes = []

while True:
    # Fråga och kovertera massan sedan lägg till i listan
    cargoes.append(float(input("Ange lastens massa: ")))

    # Om svaret INTE är "j", avsluta loopen
    if input("Vill du lägga till en ny last? (j/[n]):").lower() != "j":
        break

fuels = [fuel_consumption(cargo) for cargo in cargoes]

# Printa konsumtion med en avrundning till 2 decimaler flyttal
print(f"Förbrukning: {sum(fuels):.2f} m^3")
