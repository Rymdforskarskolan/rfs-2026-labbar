# Fråga om p och q
p = float(input("Ange p: "))
q = float(input("Ange q: "))

# Avgör ifall lösningar finns genom att beräkna värdet av diskriminanten.
# Vi vet ju att en diskriminant < 0 ger inga lösningar.
discr = (p / 2) ** 2 - q

if discr >= 0:
    # Vi beräknar båda lösningar
    sol1 = -(p / 2) + (((p / 2) ** 2 - q) ** 0.5)
    sol2 = -(p / 2) - (((p / 2) ** 2 - q) ** 0.5)

    # Om diskriminanten är noll har vi +- 0 eller dubbelrot
    if discr == 0:
        print("Lösningen är en dubbelrot:")
        print(f"x = {sol1}")  # Likvärdigt med sol2
    else:  # Här måste discr > 0 alltså två reella lösningar
        print("De två lösningarna är:")
        print(f"x1 = {sol1}")
        print(f"x2 = {sol2}")
else:  # Körs om discr < 0
    print("Inga lösningar finns!")
