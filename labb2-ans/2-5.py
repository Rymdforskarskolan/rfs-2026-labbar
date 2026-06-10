def fib(n):
    """Return the nth Fibonacci number

    Args:
        n (int): n > 0 is the index of the Fibonacci number

    Returns:
        int: The Fibonacci number n
    """

    if n < 3:
        # om n är 1 eller 2
        return 1

    # Ingen else-sats behövs för return hoppar redan ut ur funktionen
    last = 1
    last2 = 1
    # Vi är alltså på index 2
    i = 2
    while i < n:
        # Beräkna nästa
        next = last + last2

        # Lagra föregående
        last2 = last
        last = next

        # Öka index med 1
        i += 1

    # Loppen slutar när i == n dvs. när vi är klara
    # Värdet av next kommer ju då vara det vi nyss räknat ut.
    return last


print(f"fib(256): {fib(256)}")
