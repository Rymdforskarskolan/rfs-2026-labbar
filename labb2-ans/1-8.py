# Samtliga destination i uppslagsbok
destination_delta_v = {
    "Månen": 15070,
    "Merkurius": 25540,
    "Venus": 43190,
    "Neptunus": 43750,
    "Uranus": 42013,
    "Saturnus": 57340,
    "Jupiter": 78170,
}

# Initiera en tom lista för att hålla koll på destinationer
destinations = []

while True:
    # List alla destinationer genom att iterera över nycklar i uppslagsboken
    print("Destinationer:")
    for i, dest in enumerate(destination_delta_v.keys()):
        print(f"{dest}: {i}")

    # Tom rad
    print()

    # Skriv sedan ut befintliga destinationer
    print(f"Nuvarande destinationer: {destinations}")

    # Få in siffran för nästa önskad destination
    dest_num = int(input("Ange nästa destination (siffra): "))

    # Kolla giltighet av index
    if dest_num < 0 or dest_num >= len(destination_delta_v.keys()):
        print("Ogiltigt index! Försök igen.")
        # Börja om loopen
        continue

    # destination_delta_v.keys() är ju en lista av alla destinationer i ordning.
    # notera att vi måste konvertera till list för att kunna indexera
    dest = list(destination_delta_v.keys())[dest_num]

    # Spara destinationen
    destinations.append(dest)

    if input("Vill du lägga till en ny destination? (j/[n]): ").lower() != "j":
        # Om svaret INTE är "ja", avbryt loopen
        break

# Gör en lista av kostnad för alla samlade destinationer
delta_v_list = [destination_delta_v[dest] for dest in destinations]

print(f"Sammanlagd delta_v: {sum(delta_v_list)} m/s")
print(f"För destinationerna: {destinations}")
