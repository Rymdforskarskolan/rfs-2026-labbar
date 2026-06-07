# Medelvärdet av två tal
# Vi läser in två tal (kan vara flyttal) och skriver ut deras medelvärde

# Konvertera inmatning till flyttal eftersom provpoäng kan vara decimaltal
a = float(input("Ange första talet: "))
b = float(input("Ange andra talet: "))

# Beräkna medelvärdet
average = (a + b) / 2

print(f"Medelvärdet är: {average}")
