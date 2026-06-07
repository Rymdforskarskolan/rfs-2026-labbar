# Ett exempel på en meny.
menu = {
    "kaffe": 20,
    "smorreborg": 45,
    "muffin": 15,
}

item = input("Ange vara: ").strip().lower()
qty = int(input("Ange antal: "))

# Kolla att nyckeln finns
if item in menu:
    # Plocka priset, sedan multiplicera med antal
    total = menu[item] * qty
    print(f"Totalt att betala: {total} kr")
else:
    print("Fel: varan finns inte i menyn.")
