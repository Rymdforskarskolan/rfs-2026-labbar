# Läs avstånd
dist = float(input("Ange avstånd i km: "))

# Läs timme
hour = int(input("Ange timme för färd: "))

price = 200

if dist <= 5:
    price += dist * 12
else:
    # Här är dist > 5
    # Vi tar ut fullt pris för 5 km
    price += 5 * 12

    # Vi drar av de färdade km
    dist -= 5

    # Vi lägger till kostnad för kvarvarande km.
    price += dist * 8

if hour >= 22 or hour <= 6:
    # Vi lägger till 25% med förändringsfaktorn
    price *= 1.25

print(f"Priset är {price}")
