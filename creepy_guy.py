from person import Person
from staff import Staff
from mentor import Mentor

class CreepyGuy(Person, Staff):
    def __init__(self, creepiness_level, *args, **kwargs):
        self.creepiness_level = False
        super(CreepyGuy, self).__init__(*args, **kwargs)

    def arrives(self, Mentor): # creepy affect all mentors in a list
        Mentor.feeling = "nervous"
        return Mentor

    def creeping_around(self):
        self.creepiness_level = True
        return self

cg = CreepyGuy("david", "creepy", 1980, "custom", False)
print("---creepy got created---")
print(cg.creepiness_level)
mentor1 = Mentor("fg", "hobby", "david", "creepy", 1980, "custom")
print(mentor1.feeling)
cg.creeping_around()
cg.arrives(mentor1)
print("---creepy creeps---")
print(cg.creepiness_level)

print(mentor1.feeling)
