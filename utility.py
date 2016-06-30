class Utility():

    def __init__(self, name):
        self.name = name
        self.status = True

    def set_school(self, school):
        self.school = school

    def beeping(self):
        print("BEEP! BEEP!")
        self.status = False
        for mentor in self.school.mentors:
            mentor.feeling = "mad"
        print("The %s is not working." % self.name)
        return self
