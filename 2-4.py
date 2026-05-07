# Ta in ett år
year = int(input("Ange ett år: "))

if year >= 0:
    if (year % 4 == 0) and not ((year % 100 == 0) and (year % 400 != 0)):
        print("Året är ett skottår")
    else:
        print("Året är inte ett skottår")
else:
    print("Ogiltigt år!")
