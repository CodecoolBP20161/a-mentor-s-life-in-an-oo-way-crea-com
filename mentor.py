from person import Person
from staff import Staff
import os
import csv


class Mentor(Person, Staff):
    HOBBIES = ["cycling", "bouldering", "watching Star Wars"]

    def __init__(self, nickname, hobby, *args, **kwargs):
        self.nickname = nickname
        self.hobby = hobby
        super(Mentor, self).__init__(*args, **kwargs)

    @classmethod
    def create_by_csv(cls, file_name):
        mentor_list = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for line in reader:
                mentor_list.append(Mentor(line[0], line[1], line[2], line[3], line[4], line[5]))
        return mentor_list

    def check_energy(self, class_energy=None, file_name="students.csv"):
        student_energy = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                student_energy.append(int(line([5])))
            return student_energy
            #  class_energy = sum(student_energy)/len(student_energy)

    def share_knowledge(self):
        self.feeling = "proud"

mentor = Mentor("Dorci", "cycling", "Dori", "Med", 1990, "female")
# mentor.check_energy("students.csv")
# print(student_energy)
mentor_list = Mentor.create_by_csv("students.csv")
print(mentor_list[0].first_name)
print(mentor_list[1].hobby)
