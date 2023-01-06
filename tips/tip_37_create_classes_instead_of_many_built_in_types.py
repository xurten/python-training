# Tip 37 create classes instead of many built in types
# use namedtuple for small containers that will not change
# default dictionary for for creating advance dictionaries
from collections import namedtuple, defaultdict

Grade = namedtuple('Grade', ('score', 'weight'))


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)

    def student(self, name):
        return self._students[name]


book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.get_subject('math')
math.report_grade(80, 0.10)
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)
gym = albert.get_subject('WF')
gym.report_grade(100, 0.4)
gym.report_grade(85, 0.6)
print(round(albert.average_grade(), 2))
