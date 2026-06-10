# Del A
def compress(string):
    # Spara nuvarande karaktär
    current_letter = string[0]

    # Det finnst 1 st av nuvarande karaktär
    count = 1

    # Vi är nu på index 0 i strängen
    idx = 0

    # Resultatet kommer fyllas på här
    result = ""

    # Medan vår sökning är innanför längden av strängen
    while idx + count < len(string):
        # Om bokstaven på index idx + antal av nuvarande bokstav
        # är samma som nuvarande bokstav
        if string[idx + count] == current_letter:
            # Då har vi ju en till sådan bokstav
            count += 1
        else:
            # Annars har vi bytt bokstav

            # Om vi har mer än 1 av nuvarande bokstav
            if count > 1:
                # Tryck till svaret bokstaven och antal
                result += current_letter + str(count)
            else:
                # Annars bara bosktaven
                result += current_letter

            # Vårt nästa ställe att kolla är ju count platser framåt
            idx += count

            # Vi har nu till en börjar 1 st av nya bokstaven
            count = 1

            # Här plockar vi också ut nästa bokstav
            current_letter = string[idx]

    # Loopen kommer alltid brytas pga. while-kriteriet innan sista else-satsen kan köras
    # Därför gör vi sista komprimeringen efter.
    if count > 1:
        result += current_letter + str(count)
    else:
        result += current_letter

    # Vi returnerar resultatet vi har byggt.
    return result


# string = input("Ange sträng: ")
# print(compress(string))

# Del B

NUMBERS = "1234567890"


def inflate(string):
    # Börja på index 0
    idx = 0

    # Resultatet fylls på här
    result = ""

    # Fortsätt medan vi kan avsöka nästa karaktär
    while idx + 1 < len(string):
        # Regga den karaktären vi behandlar
        current_char = string[idx]

        # Om nästa är en siffra
        if string[idx + 1] in NUMBERS:
            # Vi har just nu 1 siffra på rad
            num_count = 1

            # Meda vi kan kolla 1 + num_count framåt
            # och medan denna plats OCKSÅ är en siffra
            while (idx + 1 + num_count < len(string)) and (
                string[idx + 1 + num_count] in NUMBERS
            ):
                # Öka antalet upptäckta siffror med 1
                num_count += 1

            # Vi stoppar på lika mycket bokstäver som den inlästa siffran
            # Jag har valt att använda slice igen här för att plocka ut en delsträng
            # Kolla boken eller internet eller fråga Marcell för beskrivning
            result += current_char * int(string[idx + 1 : idx + 1 + num_count])
            # Framåt med antalet siffror vi upptäckte
            idx += 1 + num_count
        else:
            # Annars är det ensam bokstav som läggs till
            result += current_char
            idx += 1

    return result


string = input("Ange sträng: ")
print(inflate(string))
