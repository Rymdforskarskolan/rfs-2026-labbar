# Fråga efter ett tal och gör om till heltal
num = int(input("Ange ett heltal: "))

# Kolla om det är jämnt
# dvs. om resten vid div. med 2 är 0:
if num % 2 == 0:
    # Detta körs bara om övan uttryck är True
    print("Talet är jämnt!")
else:
    # Detta körs endast om ovan är False
    # Vad skulle hända om vi skrev nedan print() utan else-sats?
    print("Talet är udda!")
