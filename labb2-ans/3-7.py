class SpaceStationModule:
    def __init__(self, name, crew_capacity, power_consumption):
        self.name = name
        self.crew_capacity = crew_capacity
        self.power_consumption = power_consumption

    def __str__(self):
        # Detta för en snygg print i SpaceStation.print_summary()
        return self.name

    def __repr__(self):
        # Detta är en annan typ av print, fråga Marcell :)
        return self.__str__()


class SpaceStation:
    def __init__(self, name: str, modules: list[SpaceStationModule] = []):
        self.name = name
        self.modules = modules

    def add_module(self, module: SpaceStationModule):
        self.modules.append(module)

    def remove_module(self, name):
        # Index för modul att ta bort, från början inget (None)
        idx = None

        # Kör igenom alla moduler
        for i, mod in enumerate(self.modules):
            # Om namn stämmer
            if mod.name == name:
                # Sätt idx till det index där namnet hittades
                idx = i
                # Vi behöver inte leta mer när vi hittat
                break

        # Om vi satte ett rätt index
        if idx is not None:
            # Ta bort den modulen
            del self.modules[idx]

    def print_summary(self):
        print(f"Rymdstation {self.name}:")
        print(f"Moduler: {self.modules}")
        print(
            f"Total elförbrukning: {sum(mod.power_consumption for mod in self.modules)} W"
        )
        print(
            f"Total besättningskapacitet: {sum(mod.crew_capacity for mod in self.modules)}"
        )


modules = [
    SpaceStationModule("Science Lab", 2, 1500),
    SpaceStationModule("Crew Quarters", 15, 500),
    SpaceStationModule("Mess Hall", 5, 400),
    SpaceStationModule("Gym", 4, 600),
]
station_example = SpaceStation("RFS Station", modules)

station_example.print_summary()
