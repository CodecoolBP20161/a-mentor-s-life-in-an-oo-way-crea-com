from person import Person


class Staff():
    def __init__(self):
        pass

    def set_school(self, school):
        self.school = school

    def checking_progress(self):
        self.feeling = "proud"
        print("{} checked progress and now feeling {}.".format(self.first_name, self.feeling))
        return self

    def feedback(self):
        self.feeling = "happy"
        print("{} gave feedback and now feeling {}.".format(self.first_name, self.feeling))
        if hasattr(self, "creepiness_level"):
            self.creepiness_level = False
            print("{}'s creepiness is reduced.".format(self.first_name))
        else:
            pass
        return self
