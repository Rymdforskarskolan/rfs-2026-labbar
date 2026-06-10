energy_level = 100  # %
print(f"Nuvarande laddning: {energy_level}%")
while True:
    menu_choice = input("Ladda eller skada ([l] / s): ").lower()

    match menu_choice:
        case "" | "l":
            # Vid laddning tar vi nuvarande + antal eller 100, vad som än är minst.
            energy_level = min(energy_level + float(input("Ange laddning (%):")), 100)

        case "s":
            # Vid skada tar vi nuvarande - antal eller 0, vad som än är störst.
            energy_level = max(energy_level + float(input("Ange skada (%):")), 0)

        case _:
            print("Ogiltigt val!")
            continue

    print(f"Nuvarande laddning: {energy_level}%")
