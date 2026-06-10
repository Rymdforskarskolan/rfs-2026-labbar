ALPHABET = "abcdefghijklmnopqrstuvwxyzåäö"


def encrypt(string) -> str:
    res = ""
    for letter in string:
        if letter in ALPHABET:
            res += ALPHABET[(ALPHABET.index(letter) + 3) % len(ALPHABET)]
        else:
            res += letter
    return res


cleartext = input("Ange medellandet: ")
ciphertext = encrypt(cleartext)

print(f"Kodat meddelande: {ciphertext}")
