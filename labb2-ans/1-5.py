energy_level = 100  # %
print(f"Nuvarande laddning: {energy_level}%")
while True:
    menu_choice = input("Ladda eller skada ([l] / s): ").lower()

    match menu_choice:
        case "" | "l":
            energy_level += float(input("Ange laddning (%):"))

        case "s":
            energy_level -= float(input("Ange skada (%):"))

        case _:
            print("Ogiltigt val!")
            continue

    print(f"Nuvarande laddning: {energy_level}%")
