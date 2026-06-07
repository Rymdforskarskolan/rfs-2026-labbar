age = int(input("Ange ålder: "))

# Kom ihåg att if-elif-kedjor kortsluter, första giltiga alternativet är det ENDA som körs.
if age < 0:
    print("Fel: åldern kan inte vara negativ.")
elif age < 15:
    price = 90
elif age < 18:
    price = 110
else:
    price = 140

print(f"Biljettpris: {price} kr")
