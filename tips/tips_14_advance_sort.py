# Tip 14 advance sorting

class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __repr__(self):
        return f'Student({self.name}, {self.mark})'


students = [
    Student('andrzej', 5),
    Student('jan', 2),
    Student('kasia', 6),
    Student('magda', 3),
    Student('bartek', 1)
]

places = ['House', 'PARK', 'desert', 'forest', 'Mountains']


def sort_student_by_name():
    students.sort(key=lambda x: x.name)
    print(students)


def sort_student_by_mark():
    students.sort(key=lambda x: x.mark, reverse=True)
    print(students)


def sort_places():
    places.sort(key=lambda x: x.upper())
    print(places)


def sort_student_by_mark_and_name():
    students.sort(key=lambda x: (x.mark, x.name))
    print(students)


def sort_student_by_name_and_mark():
    students.sort(key=lambda x: (x.name, x.mark))
    print(students)


sort_student_by_name()
sort_student_by_mark()
sort_places()
sort_student_by_mark_and_name()
sort_student_by_name_and_mark()