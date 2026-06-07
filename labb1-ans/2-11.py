# Välj djur
# Lista tre djur och låt användaren välja via index 0-2

animals = ["Hund", "Katt", "Kaninen"]

# idx är sedvanligt namn för att lagra index
# Index är givetvis heltal här
idx = int(input("Välj ett index 0-2: "))

# Här kollas om index är giltigt.
# Tänk på att index är 0-baserat! Så 0, 1, 2 är ok.
# len() ger antal element, dvs. 3
if 0 <= idx < len(animals):
    print(f"Du valde: {animals[idx]}")
else:
    print("Fel: index utanför intervallet 0-2.")
