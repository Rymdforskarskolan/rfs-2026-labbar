class Time:
    def __init__(self, hour, minute, second):
        # Normalisera tiden genom att räkna om allt till sekunder
        total = hour * 3600 + minute * 60 + second

        # Åk runt vid ett dygn
        total %= 24 * 3600

        # Avrunda ned till närmsta timme
        self.hour = total // 3600

        # Mod 1 tim
        total %= 3600

        # Avrunda till närmsta min
        self.minute = total // 60

        # Mod 1 min
        self.second = total % 60

    def __add__(self, other):
        # Räkna om till totalt antal sekunder, addera och låt tiden åka runt ett dygn
        total = (self.total_seconds() + other.total_seconds()) % (24 * 3600)

        # Avrunda till närmsta timme ned
        hour = total // 3600

        # Mod 1 tim
        total %= 3600

        # Närmsta antal minuter
        minute = total // 60

        # Mod 1 min
        second = total % 60

        return Time(hour, minute, second)

    def __sub__(self, other):
        # Räkna om till totalt antal sekunder, subtrahera och låt tiden åka runt ett dygn
        diff = (self.total_seconds() - other.total_seconds()) % (24 * 3600)

        # Avrunda till närmsta timme ned
        hour = diff // 3600

        # Mod 1 tim
        diff %= 3600

        # Närmsta antal minuter
        minute = diff // 60

        # Mod 1 min
        second = diff % 60

        return Time(hour, minute, second)

    def total_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def __gt__(self, other):
        return self.total_seconds() > other.total_seconds()

    def __lt__(self, other):
        return self.total_seconds() > other.total_seconds()

    def __eq__(self, other):
        return self.total_seconds() > other.total_seconds()

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"
