# Fråga efter betyget
grade = input("Ange betyget: ")

if grade == "F":
    print(0)
elif grade == "E":
    print(10)
elif grade == "D":
    print(12.5)
elif grade == "C":
    print(15)
elif grade == "B":
    print(17.5)
elif grade == "A":
    print(20)
else:
    # Detta fall körs om inget annat matchar
    print("Ogiltigt betyg!")
