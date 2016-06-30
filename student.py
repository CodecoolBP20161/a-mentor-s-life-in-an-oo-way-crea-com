from person import Person
import os
import csv


class Student(Person):
    CONFIDENCES = ["none", "low", "medium", "high", "super"]
    knowledge = [x for x in range(1, 11)]

    def __init__(self, knowledge_level, confidence, *args, **kwargs):
        self.confidence = self.CONFIDENCES[0]
        self.knowledge_level = 1
        super(Student, self).__init__(*args, **kwargs)

    @classmethod
    def create_by_csv(cls, file_name):
        student_list = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for line in reader:
                student_list.append(Student(line[0], line[1], line[2], line[3], line[4], line[5]))
        return student_list

    def dojo(self):
        for i in range(0,len(self.CONFIDENCES)-1):
            if self.confidence == self.CONFIDENCES[i]:
                self.confidence = self.CONFIDENCES[i+1]
                break
        return self

student = Student("Dóri","Med",1990,"female","neutral",1)
student.dojo()
student.dojo()
print(student.confidence)
