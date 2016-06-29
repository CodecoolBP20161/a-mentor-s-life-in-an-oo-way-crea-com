class Person:
    FEELINGS = ["neutral", "satisfied", "happy", "sad", "proud", "nervous", "mad", "energized", "uncomfortable"]
    ENERGY_LEVELS = [x for x in range(1, 11)]

    def __init__(self, first_name, last_name, year_of_birth, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.energy_level = 1
        self.feeling = "neutral"

    def drink_coffee(self):
        self.feeling = "energized"
        self.energy_level += 2
        return self

    def lunch_break(self):
        self.energy_level += 2
        # + codecool_class attention!!
        return self
