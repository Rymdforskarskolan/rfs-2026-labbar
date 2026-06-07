month = input("Ange månad (t.ex. januari): ").strip().lower()
# .strip(): ta bort onödig whitespace före/efter en sträng.
# .lower(): gör så att hela strängen är i gemener.

days_in_month = {
    "januari": 31,
    "februari": 28,
    "mars": 31,
    "april": 30,
    "maj": 31,
    "juni": 30,
    "juli": 31,
    "augusti": 31,
    "september": 30,
    "oktober": 31,
    "november": 30,
    "december": 31,
}

# Vi kollar om månaden existerar som nyckel i dict:en
if month in days_in_month:
    # Vi printar sedan månadens namn med antal dagar hämtat från dict:en
    print(f"{month.capitalize()} har {days_in_month[month]} dagar.")
    # .capitalize(): Gör först bokstaven i varje ord versal.
else:
    print("Fel: okänd månad.")
