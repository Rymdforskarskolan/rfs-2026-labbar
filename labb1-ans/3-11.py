def prime_factors(n):
    """
    Return a list with the prime factors of n in non-decreasing order.

    This function uses simple trial division which is fine for moderate n.
    """
    # Skapa en tom lista att hålla koll på faktorer
    factors = []

    # Ta bort alla faktorer 2
    while n % 2 == 0:
        factors.append(2)
        # Vi dividerar med trunkerande division, då vi är säkra på att det går jämt ut.
        # Detta krävs så att resultatet är av typen int och inte möjligtvis float.
        n //= 2

    # Här testar vi alla udda tal f.o.m. 3 tills vi är klara.
    # Kom ihåg att ett tal a är prim om a % b != 0 för alla b != a, 1
    # Vi behöver enligt matten bara kolla alla b < sqrt(a) eller b**2 < a
    f = 3
    while f**2 <= n:
        # Medan du kan dela med den nuvarande faktorn, ta bort den.
        while n % f == 0:
            factors.append(f)
            n //= f

        # Gå till nästa udda tal
        f += 2

    # Om talet inte är 1, lägg till resten.
    if n > 1:
        factors.append(n)
    return factors


# Huvudprogram
n = int(input("Ange ett heltal (>1): "))
if n <= 1:
    print("Fel: talet måste vara större än 1.")
else:
    facs = prime_factors(n)

    # Skriv ut i formatet: 12 -> 2, 2, 3
    # Kom ihåg .join() som tar element i en kollektion och klistrar
    # ihop dem med den angivna strängen mellan.
    facs_str = ", ".join(str(x) for x in facs)
    #                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #                         spicy syntax, kommer senare
    # Sist skrier vi ut slutresultatet
    print(f"{n} -> {facs_str}")
