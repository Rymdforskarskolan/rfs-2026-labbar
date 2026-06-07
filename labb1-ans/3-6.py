# Ett exempel på godtagbara värden
phonebook = {
    "Anna": "070-123 54 88",
    "Bertil": "070-327 68 46",
    "Cecilia": "076-321 48 68",
}

name = input("Ange namn att söka: ")

# Kolla om nyckeln finns
if name in phonebook:
    print(f"{name}: {phonebook[name]}")
else:
    print("Personen saknas i telefonboken.")
