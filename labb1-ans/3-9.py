birth_year = int(input("Ange födelseår: "))
age_now = int(input("Ange nuvarande ålder: "))

if birth_year < 0 or age_now < 0:
    print("Fel: negativa värden är inte tillåtna.")
else:
    CURRENT_YEAR = 2026
    # Beräknat ålder utan hänsyn till födelsedagsskillnad
    expected_age = CURRENT_YEAR - birth_year
    # Tillåt en differens på 1 år (före/efter födelsedag)
    # Här tar vi alltså absolutbeloppet av diff:en i ålder.
    if abs(expected_age - age_now) > 1:
        print("Fel: födelseår och ålder verkar inte stämma överens.")
    else:
        # Här kollar vi om de är mer än 18 år om 10 år.
        will_be_adult = (age_now + 10) >= 18
        print(f"Ser rimligt ut. Om 10 år är personen myndig: {will_be_adult}")
