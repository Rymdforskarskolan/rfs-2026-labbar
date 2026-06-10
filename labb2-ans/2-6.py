def is_prime(n):
    # Tecken på n spelar ingen roll
    n = abs(n)

    # Kända gränsfall
    if n == 1 or n == 2:
        return True

    # Vi kollar alla heltal f.o.m. 2 t.o.m. n-1
    for i in range(2, n):
        # Om något går att dela jämt => False
        if n % i == 0:
            return False

    # Om vi fortfarande är kvar efter att ha kollat allt, så True
    return True


# Alla tal från 2-50
for n in range(2, 51):
    if is_prime(n):
        print(n)
