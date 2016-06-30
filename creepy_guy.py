from person import Person
from staff import Staff
from mentor import Mentor


class CreepyGuy(Person, Staff):
    def __init__(self, creepiness_level, *args, **kwargs):
        self.creepiness_level = False
        super(CreepyGuy, self).__init__(*args, **kwargs)

    def arrives(self):
        for mentor in self.school.mentors:
            mentor.feeling = "nervous"
        print("{} arrives and makes everyone {}.".format(self.first_name, mentor.feeling))
        return Mentor

    def creeping_around(self):
        self.creepiness_level = True
        print("{} is creeping around.".format(self.first_name))
        return self
