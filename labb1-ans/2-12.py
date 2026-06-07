year = int(input("Ange ett år: "))

if year >= 0:
    # (delbart med 4?) och ej ((delbart med 100?) och (ej delbart m. 400?))
    if (year % 4 == 0) and not ((year % 100 == 0) and (year % 400 != 0)):
        print("Året är ett skottår")
    else:
        print("Året är inte ett skottår")
else:
    print("Ogiltigt år!")
