class Person(object):
    FEELINGS = ["sad", "mad", "uncomfortable", "nervous", "neutral", "satisfied", "happy", "energized", "proud"]
    ENERGY_LEVELS = [x for x in range(1, 11)]

    def __init__(self, first_name, last_name, year_of_birth, gender, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.energy_level = 1
        self.feeling = "neutral"
        super(Person, self).__init__(*args, **kwargs)

    def set_school(self, school):
        self.school = school

    def drink_coffee(self):
        self.feeling = "energized"
        self.energy_level += 2
        print("{} loves coffee and gets {}.".format(self.first_name, self.feeling))
        return self

    def lunch_break(self):
        self.energy_level += 2
        self.school.attention = True
        print("Let's get lunch break!")
        return self
