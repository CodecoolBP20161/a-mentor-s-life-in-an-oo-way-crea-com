from person import Person


class Staff(Person):
    def __init__(self, *args, **kwargs):
        super(Staff, self).__init__(*args, **kwargs)

    def checking_progress(self):
        self.feeling = "proud"
        return self

    def feedback(self):
        self.feeling = "happy"
        if hasattr(self, "creepiness_level"):
            self.creepiness_level = False
        else:
            pass
        return self
