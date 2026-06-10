class Colony:
    def __init__(self, name, population, growth_rate):
        """Instantiate a new Colony

        Args:
            name (str): Name of the colony
            population (int): Number of residents
            growth_rate (int): Change in number of colonists per annum
        """
        self.name = name
        self.population = population
        self.growth_rate = growth_rate

    def advance_year(self):
        """Calculate and apply population change for 1 year"""
        self.population += self.growth_rate


# Vi skapar en list av våra kolonier
colonies = [
    Colony("New Mars", 100000, 3000),
    Colony("Moon Base Alpha", 300, 20),
    Colony("Ceres Station", 650, 400),
]

for i in range(3):
    # Vi itererar alltså över värden av typ Colony
    for colony in colonies:
        # Vi anropar metoden på varje koloni i listan
        colony.advance_year()

for colony in colonies:
    print(f"Population på {colony.name}: {colony.population}")
