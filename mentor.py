import os
import csv
import random
from person import Person
from staff import Staff
from student import Student
from utility import Utility


class Mentor(Person, Staff):

    def __init__(self, nickname, hobby, *args, **kwargs):
        self.nickname = nickname
        self.hobby = hobby
        super(Mentor, self).__init__(*args, **kwargs)
        print("{} {} is alive.".format (self.first_name, self.last_name))

    @classmethod
    def create_by_csv(cls, file_name):
        mentor_list = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for line in reader:
                mentor_list.append(Mentor(line[0], line[1], line[2], line[3], line[4], line[5]))
        return mentor_list

    def check_knowledge(self):
        student_knowledge = []
        for student in self.school.students:
            student_knowledge.append(student.knowledge_level)
        class_knowledge = int(sum(student_knowledge) / len(student_knowledge))
        print("The knowledge level is %d" % class_knowledge)
        return self

    def share_knowledge(self):
        self.feeling = "proud"
        for student in self.school.students:
            student.knowledge_level += 1
        if self.energy_level > 1:
            self.energy_level -= 2
        print("{} shared his knowledge.".format(self.nickname))
        return self

    def do_hobby(self):
        self.feeling = random.choice(Person.FEELINGS)
        if self.feeling in Person.FEELINGS[0:4]:
            print("I feel {}, let's do {} !".format(self.feeling, self.hobby))
            self.feeling = "happy"
            print("It's much better to be {}.".format(self.feeling))
        else:
            print("It's OK, I feel {}.".format(self.feeling))
        return self

    def gong(self):
        self.school.attention = True
        print("Let's get some attention... GOOOONG!!!")
        return self

    def check_attendance(self):
        if self.school.attendance in self.school.ATTEND[0:3]:
            self.feeling = "sad"
            print("The school's attendance status is {}, it's so {}.".format(self.school.attendance, self.feeling))
        else:
            self.feeling = "satisfied"
            print("The school's attendance status is {}, I feel {}.".format(self.school.attendance, self.feeling))
        return self

    def maintain_utility(self, utility):
        print("The {} is broken, I feel {}.".format(utility.name, self.feeling))
        utility.status = True
        self.feeling = "satisfied"
        print("The {} is working again! I feel {}.".format(utility.name, self.feeling))
        return self
