import time

oxygen_left = 100  # %
oxygen_per_second = -16 / 60  # % / s

# Lagra förra gånge vi gjorde nåt med syrehalten
last_time = time.time()

while True:
    if oxygen_left <= 0:
        # Avbryt om syret är slut
        break

    # Syrehalt avrundad till 1 decimal

    # Om det gått mer än 1 sekund sen sist
    if time.time() - last_time > 1:
        oxygen_left += oxygen_per_second
        # Förra gången var nu.
        last_time = time.time()
        # Print inom if-satsen så att vi inte spammar terminalen
        print(f"Nuvarande syrehalt: {oxygen_left:.1f} %")
