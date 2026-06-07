# Ta in ett antal dagar
days = int(input("Hur många dagar är boken försenad? "))

if days < 0:
    print("Fel: antalet dagar kan inte vara negativt.")
else:
    if days <= 7:
        fee = days * 2
    else:
        fee = 7 * 2 + (days - 7) * 5
    print(f"Förseningsavgift: {fee} kr")
