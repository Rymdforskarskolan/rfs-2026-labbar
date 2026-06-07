# Färgkod med uppslag
# Lagra färger och korta beskrivningar i en dict och slå upp

colors = {
    "röd": "Värmande, varningsfärg.",
    "grön": "Associeras ofta med säkerhet och natur.",
    "blå": "Kall färg, ger ofta intryck av lugn.",
}

color_input = input("Ange en färg: ").strip().lower()

if color_input in colors:
    print(colors[color_input])
else:
    print("Färgen saknas i manualen.")
