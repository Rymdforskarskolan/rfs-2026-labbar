# Läs indata som siffror
day = int(input("Ange dag (1-31): "))
month = int(input("Ange månad (1-12): "))
year = int(input("Ange år (t.ex. 2026): "))

# Negativa år är ju omöjliga
if year < 0:
    print("Fel: årtal måste vara icke-negativt.")
else:
    # En dict (uppslagstabell, lookup-tabel) över antal dagar i varje månad.
    # Detta hade kunna vara en list, men dict är mer idiomatiskt.
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    # Om månadens nummer inte finns som nycekl
    if month not in days_in_month:
        print("Fel: ogiltig månad.")
    elif day < 1 or day > days_in_month[month]:
        # Om dagen är för liten eller för stor för den givna månaden
        print("Fel: ogiltig dag för den angivna månaden.")
    else:
        print("Datumet är giltigt.")
