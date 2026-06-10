ALPHABET = "abcdefghijklmnopqrstuvwxyzåäö"


def decrypt(string) -> str:
    res = ""
    for letter in string:
        if letter in ALPHABET:
            res += ALPHABET[(ALPHABET.index(letter) - 3) % len(ALPHABET)]
        else:
            res += letter
    return res


ciphertext = input("Ange det krypterade medellandet: ")
cleartext = decrypt(ciphertext)

print(f"Avkodat medellande: {cleartext}")
