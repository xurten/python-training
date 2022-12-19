# Tip 46 use descriptors for multyply methods with property
from weakref import WeakKeyDictionary


class Homework:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Must be from 0 to 100')
        self._grade = value

    def __repr__(self):
        return f'{self.grade}'


galileo = Homework()
galileo.grade = 95
print(galileo)


class Exam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Must be from 0 to 100')


# with descriptor
class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Must be from 0 to 100')
        self._value[instance] = value


class Second_Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
print(f'{first_exam.writing_grade} {second_exam.writing_grade}')
