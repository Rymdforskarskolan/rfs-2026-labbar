day_num = int(input("Ange ett tal 1-7 för veckodag (1=måndag): "))

match day_num:
    case 1:
        print("Måndag")
    case 2:
        print("Tisdag")
    case 3:
        print("Onsdag")
    case 4:
        print("Torsdag")
    case 5:
        print("Fredag")
    case 6:
        print("Lördag")
    case 7:
        print("Söndag")
    case _:
        print("Fel: talet måste vara mellan 1 och 7.")
