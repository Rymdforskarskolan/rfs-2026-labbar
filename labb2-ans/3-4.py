import random


class RockPaperScissorsPlay:
    VALID_PLAYS = ["sten", "sax", "påse"]

    def __init__(self, type):
        if type not in self.VALID_PLAYS:
            print("Du har angett fel typ!")
            self.type = None
        else:
            self.type = type

    @classmethod
    def random(cls):
        return cls(random.choice(cls.VALID_PLAYS))

    def wins_against(self, other):
        # Matcha på egen typ
        match self.type:
            case "sten":
                # Sten vinner mot sax => True
                if other.type == "sax":
                    return True
            case "sax":
                # Sax vinner mot påse => True
                if other.type == "påse":
                    return True
            case "påse":
                # Påse vinner mot sten => True
                if other.type == "sten":
                    return True

        # Om inte något av de if kördes, måste vi ha förlorat
        return False


player_score = 0
computer_score = 0
for _ in range(3):
    # Variabeln definieras här för att den skall vara i rätt block
    play = None

    while True:
        # Be om drag
        play = input("Ange ditt drag (sten/sax/påse): ")

        # Om draget finns i listan av giltiga, sluta fråga
        if play in RockPaperScissorsPlay.VALID_PLAYS:
            play = RockPaperScissorsPlay(play)
            break

    computer_play = RockPaperScissorsPlay.random()

    if play.wins_against(computer_play):
        player_score += 1
        print(
            f"Du vann draget! ({play.type} mot {computer_play.type}) {player_score}-{computer_score}"
        )
    else:
        computer_score += 1
        print(
            f"Du förlorade draget! ({play.type} mot {computer_play.type}) {player_score}-{computer_score}"
        )

if player_score > computer_score:
    print("Du vann matchen!")
else:
    print("Du förlorade matchen tyvärr :(")
