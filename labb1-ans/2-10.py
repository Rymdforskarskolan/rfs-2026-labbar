# Gör ett rimligt antagande på godkända färger och gör en mängd.
allowed = {"röd", "grön", "blå", "gul", "svart"}

color = input("Ange färg: ").strip().lower()
# .strip(): Rensa whitespace före/efter en sträng
# .lower(): Samtliga bokstäver som gemener.

# Kolla om färgen tillhör mängden av tillåtna färger
if color in allowed:
    print("Färgen är tillåten.")
else:
    print("Färgen är inte tillåten.")
