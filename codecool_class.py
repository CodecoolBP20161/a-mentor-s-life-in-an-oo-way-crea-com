from mentor import Mentor
from student import Student
import datetime
import csv
import random


class CodecoolClass:
    ATTEND = ["nobody", "poor", "fair", "medium", "good", "full_house"]

    def __init__(self, location, year=None, day=None, mentors=None, students=None):
        self.location = location
        self.year = datetime.date.today().year
        self.day = (datetime.datetime.now()).strftime("%A")
        self.mentors = Mentor.create_by_csv("mentors.csv")
        self.students = Student.create_by_csv(create_by_csv("students.csv"))
        self.attendance = self.ATTEND[random.randint(0, len(self.ATTEND)-1)]

        self.knowledge = []
        for student in self.students:
            knowledge.append(int(student[7]))
        self.knowledge = int(sum(knowledge) / len(knowledge))

        self.attention = False

        self.energy = []
        for student in self.students:
            energy.append(int(student[5]))
        self.energy = int(sum(energy) / len(energy))

    @classmethod
    def generate_local(cls):
        cls.location = "Budapest"
        cls.year = 2016
        cls.day = "Monday"
        cls.mentors = Mentor.create_by_csv("mentors.csv")
        cls.students = Student.create_by_csv(create_by_csv("students.csv"))
        cls.attendance = cls.ATTEND[random.randint(0, len(cls.ATTEND)-1)]
        cls.knowledge = 5
        cls.attention = False
        cls.energy = 1
        return cls

    def find_mentor_by_full_name(self, full_name):
        for mentor in self.mentors:
            if mentor.first_name + mentor.last_name == full_name.replace(" ", ""):
                return mentor

    def find_student_by_full_name(self, full_name):
        for student in self.students:
            if student.first_name + student.last_name == full_name.replace(" ", ""):
                return student
