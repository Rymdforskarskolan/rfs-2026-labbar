weight = float(input("Ange paketets vikt i kg: "))

if weight <= 2:
    cost = 49
elif weight <= 5:
    cost = 79
else:
    cost = 119

print(f"Fraktkostnad: {cost} kr")
