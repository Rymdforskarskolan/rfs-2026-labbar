import time
import random


class Cell:
    def __init__(self, has_asteroid=False, has_spaceship=False):
        self.has_asteroid = has_asteroid
        self.had_spaceship = has_spaceship


class AsteroidField:
    def __init__(self, asteroids: list[list[Cell]]):
        self.cells = asteroids

    @classmethod
    def random(cls):
        # Skapa en 10x10 lista fyllt av Cell
        # Varje cell tar default: inget skepp, ingen asteroid
        asteroids = [[Cell() for _ in range(10)] for _ in range(10)]

        for row in range(10):
            for col in range(10):
                if col == 0:
                    # Inga asteroider på första kolumnen
                    continue

                # random.random() ger 0 < x < 1.0.
                # >= 0.6 ger 30% chans
                if random.random() >= 0.7:
                    # Om ja, asteroid
                    asteroids[row][col] = Cell(has_asteroid=True)
                # else: behåller vi ju False som redan är där

        # Returnera en ny instans med det fältet vi genererade
        return cls(asteroids)

    def is_asteroid_in_front(self, row, col):

        # Om koordinaten är utanför kartan, nej
        if col > 9:
            return False

        # Kolla asteroids existens 1 column fram
        return self.cells[row][col + 1].has_asteroid

    def is_asteroid_above(self, row, col):
        # Om koordinaten är utanför kartan, nej
        if row - 1 < 0:
            return False

        # Kolla asteroids existens 1 column fram
        return self.cells[row - 1][col].has_asteroid

    def is_asteroid_below(self, row, col):
        # Om koordinaten är utanför kartan, nej
        if row + 1 > 9:
            return False

        # Kolla asteroids existens 1 column fram
        return self.cells[row + 1][col].has_asteroid

    # Minns ni, såhär gör vi klassen print() kompatibel
    def __str__(self):
        result = ""
        for row in self.cells:
            for cell in row:
                if cell.has_asteroid:
                    # fylld ruta, ingen nyrad efter
                    result += "[O] "
                elif cell.had_spaceship:
                    result += "[X] "
                else:
                    # tom ruta
                    result += "[ ] "

            # Körs en gång per rad
            # Sätter dit blankrad
            result += "\n"

        # Return när allt är färdigt
        return result


class SpaceShip:
    def __init__(self):

        self.direction = "up"

    def navigate(self, asteroid_field=None, start_row=None):
        # Om inget fält angavs random
        if asteroid_field is None:
            self.field = AsteroidField.random()
        else:
            self.field = asteroid_field

        # Om ingen rad angavs, random
        if start_row is None:
            self.row = random.randint(0, 9)
        else:
            self.row = start_row

        # Start alltid från vänster
        self.col = 0

        # Räknare för försök
        i = 1
        MAX_TRIES = 30
        # Medan move() inte ger True för färdigt
        while not self.move():
            if i > MAX_TRIES:
                # Om vi har mer än 30 försök, sluta
                print("Lyckades inte :(")
                break

            print(f"Försök {i}/{MAX_TRIES}")
            i += 1
            print(self.field)
            # 1 move per 0.2 sek, så det inte spammas
            time.sleep(0.2)

        print("Färdig!")
        print(self.field)

    def move(self):
        """Move the ship, return True if finished"""

        # Notera att skeppet varit här
        self.field.cells[self.row][self.col].had_spaceship = True

        if self.col >= 9:
            # Kolumn 9 är klart, True
            return True

        # Om framåt krockar
        if self.field.is_asteroid_in_front(self.row, self.col):
            # Om vi skall uppåt
            if self.direction == "up":
                # Om raden ovanför är inom rutan
                # och om det inte finns asteroid ovan
                if (self.row - 1 >= 0) and not self.field.is_asteroid_above(
                    self.row, self.col
                ):
                    # Flytta 1 rad upp
                    self.row -= 1
                else:
                    # Annars byt riktning
                    self.direction = "down"
            elif self.direction == "down":
                # Om raden nedanför är inom rutan
                # och om ingen asteroid nedanför
                if (self.row + 1 < 10) and not self.field.is_asteroid_below(
                    self.row, self.col
                ):
                    # Flytta en rad ned
                    self.row += 1
                else:
                    # Annars byt riktning
                    self.direction = "up"
        else:
            # Annars är det fritt fram
            self.col += 1

        # Inte färdig än
        return False


# Skapa ett SpaceShip
ship = SpaceShip()
# Navigera ett random fält från en random rad
ship.navigate()
