# from person import Person


class Utility():

    def __init__(self, name):
        self.name = name
        self.status = True

    def beeping(self):
        self.status = False
        print("The %s is not working." % self.name)
        return self
