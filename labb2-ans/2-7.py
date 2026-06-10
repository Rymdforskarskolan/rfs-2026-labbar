word = input("Ange ett ord att kolla: ")

# Detta är alltså ett slice från start -> slut med steglängd -1, dvs. baklänges
if word == word[::-1]:
    print("Ja, ett palindrom!")
else:
    print("Nej, inte ett palindrom!")


# Man kan också skriva
def is_palindrome(word):
    # Alla index i word
    for i in range(len(word)):
        # Om bokstaven vid i != bokstaven vid i bakifrån, False
        if word[i] != word[-(i + 1)]:
            return False

    # Om alla bokstäver stämmer, True
    return True
