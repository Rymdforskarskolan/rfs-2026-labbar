# Ta in priset, som kan ha bråkdels kronor
price = float(input("Ange priset (kr): "))

# Vi läsar in ett tal, användare behöver inte ange procenttecken
discount_percent = float(input('Ange rabatt i procent (utan procenttecken, "%"): '))

# Få rabatten som förändringsfaktor
discount_fraction = discount_percent / 100

# Beräkna det nya priset m.h.a. f.f.
new_price = price * (1 - discount_fraction)

print(f"Pris efter rabatt: {new_price}")
