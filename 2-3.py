# Fråga om poängen
points = float(input("Ange förvärvade poäng: "))

# Python är fiffigt och tillåter "matematisk" intervallnotation för tal.
if 0 <= points <= 100:
    if points < 50:
        print("F")
    elif 50 <= points < 60:
        print("E")
    elif 60 <= points < 70:
        print("D")
    elif 70 <= points < 80:
        print("C")
    elif 80 <= points < 90:
        print("B")
    else:  # Nu har vi uteslutit allt annat, så endast else behövs
        print("A")
