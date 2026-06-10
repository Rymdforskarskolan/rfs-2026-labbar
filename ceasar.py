#! /usr/bin/env python3
import string

alphabet = string.ascii_lowercase + "åäö"


def encrypt(string) -> str:
    res = ""
    for letter in string:
        if letter in alphabet:
            res += alphabet[(alphabet.index(letter) + 3) % len(alphabet)]
        else:
            res += letter
    return res


def decrypt(string) -> str:
    res = ""
    for letter in string:
        if letter in alphabet:
            res += alphabet[(alphabet.index(letter) - 3) % len(alphabet)]
        else:
            res += letter
    return res


def main():
    mode = input("Avkoda / Kryptera ([a]/k): ").lower()
    message = input("Ange medellande: ").lower()
    match mode:
        case "a" | "A" | "":
            message = decrypt(message)
        case "k":
            message = encrypt(message)
        case _:
            print("Nu har du gjort fel!")

    print(f"Resultat: {message}")


if __name__ == "__main__":
    main()
