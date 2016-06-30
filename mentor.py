from person import Person
from staff import Staff
from student import Student
from codecool_class import CodecoolClass
import os
import csv
import random

class Mentor(Person, Staff):


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
        #class_energy = sum(student_energy)/len(student_energy)

    def share_knowledge(self):
        self.feeling = "proud"
        if self.energy_level > 1:
            self.energy_level -= 2
        return self

    def do_hobby(self, hobby):
        self.feeling = random.choice(Person.FEELINGS)
        self.hobby = hobby
        if self.feeling == "nervous":
            print("Let's do %s !" % self.hobby)
            self.feeling = "happy"
            print("I feel %s now!" % self.feeling)
        return self

    def gong(self, Codecool_class):
        Codecool_class.attention = True
        return self

    def check_attendance(self):
        if CodecoolClass.attendance in CodecoolClass.ATTEND[0:3]:
            self.feeling = "sad"
        else:
            self.feeling = "satisfied"
        return self


mentor_1 = Mentor("Miki", "cycling", "Miklos", "Beothy", 1978, "male")
student_1 = Student("Dora", "Medgyasszay", 1990,"female","neutral",1) # nem lehet példányosítani!
Mentor.check_attendance()
print(mentor_1)
