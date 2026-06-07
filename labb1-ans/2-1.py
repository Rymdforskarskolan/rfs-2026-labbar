# Fråga efter betyget
grade = input("Ange betyget: ")

match grade:
    case "F":
        print(0)
    case "E":
        print(10)
    case "D":
        print(12.5)
    case "C":
        print(15)
    case "B":
        print(17.5)
    case "A":
        print(20)
    case _:
        # Detta case körs om inget annat matchar
        print("Ogiltigt betyg!")
