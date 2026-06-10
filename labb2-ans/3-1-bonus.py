class Colonist:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def birthday(self):
        # Öka ålder med 1
        self.age += 1
        # Gratta sig själv
        print(f"Grattis på födelsedagen, {self.name}!")


class Colony:
    def __init__(self, name, colonists: list[Colonist]):
        self.name = name
        self.colonists = colonists

    def add_colonist(self, name, age, job):
        self.colonists.append(Colonist(name, age, job))

    def remove_colonist(self, name):
        idx = None
        for i, colonist in enumerate(self.colonists):
            if name == colonist.name:
                idx = i
                # Vi behöver inte kolla flear när vi hittat rätt, så break
                break

        # Om vi faktiskt bytte värde på idx
        if idx is not None:
            # Se hur vi använder del och inte list.remove()
            # Det är för att vi tar bort ett index och inte ett värde
            del self.colonists[idx]
