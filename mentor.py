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

    def set_school(self, school):
        self.school = school

    @classmethod
    def create_by_csv(cls, file_name):
        mentor_list = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for line in reader:
                mentor_list.append(Mentor(line[0], line[1], line[2], line[3], line[4], line[5]))
        return mentor_list

    def check_energy(self, file_name="students.csv"):
        student_energy = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for line in reader:
                student_energy.append(int(line[5]))
        class_energy = sum(student_energy) // len(student_energy)
        return self

    def share_knowledge(self):
        self.feeling = "proud"
        if self.energy_level > 1:
            self.energy_level -= 2
        return self

    def do_hobby(self):
        self.feeling = random.choice(Person.FEELINGS)
        if self.feeling == "nervous":
            print("Let's do %s !" % self.hobby)
            self.feeling = "happy"
        return self

    def gong(self):
        self.school.attention = True
        return self

    def check_attendance(self):
        if self.school.attendance in self.school.ATTEND[0:3]:
            self.feeling = "sad"
        else:
            self.feeling = "satisfied"
        return self

    def maintain_utility(self, utility):
        utility.status = True
        self.feeling = "satisfied"
        return self
