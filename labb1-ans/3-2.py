# Fråga om tre sidor
# Notera att jag använder mer beskrivande namn än a,b,c
side1 = float(input("Ange sida 1: "))
side2 = float(input("Ange sida 2: "))
side3 = float(input("Ange sida 3: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    # Här har vi en giltig triangel
    if side1 == side2 and side2 == side3:
        # Här har vi en liksidig triangel
        print("Du har en liksidig triangel!")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        # Här har du en likbent triangel
        # Du vet att alla sidor inte är lika, men minst två av dem är lika
        print("Du har en likbent triangel!")
    else:
        # Här har du en allmän triangel
        print("Du har en giltig triangel!")
else:
    # Här har du en ogiltig triangel som inte uppfyller triangelolikheten
    print("Dessa sidor bildar inte en triangel!")
