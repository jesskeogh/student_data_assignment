# Object orientated example

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_grade_band(self):
        if self.grade >= 70:
            return "A"
        elif self.grade >= 60:
            return "B"
        elif self.grade >= 50:
            return "C"
        else:
            return "Fail"

s = Student("Jess", 63)
print(s.get_grade_band())
