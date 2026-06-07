month = input("Ange månad (t.ex. januari): ").strip().lower()
# .strip(): ta bort onödig whitespace före/efter en sträng.
# .lower(): gör så att hela strängen är i gemener.

months_with_31 = {"januari", "mars", "maj", "juli", "augusti", "oktober", "december"}
months_with_30 = {"april", "juni", "september", "november"}

if month == "februari":
    print(f"{month.capitalize()} har 28 dagar.")
    # .capitalize(): Första bokstaven versal.
elif month in months_with_31:
    # Här kollar vi mängdtillhörighet för att se vart månaden ligger.
    print(f"{month.capitalize()} har 31 dagar.")
elif month in months_with_30:
    print(f"{month.capitalize()} har 30 dagar.")
else:
    print("Fel: okänd månad.")
