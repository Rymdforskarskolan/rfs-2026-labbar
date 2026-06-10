class Astronaut:
    def __init__(self, grade):
        self.grade = grade

    def is_ready(self):
        """True if astronaut is ready, else False"""
        return self.grade > 90
