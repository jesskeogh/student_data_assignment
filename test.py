# student class
# has first name, last name, student num
# print name

class Student(object):
    def __init__(self,name, last_name, student_id):
        self.name = name
        self.last_name = last_name
        self.student_id = student_id

    def show_name(self):
        print(self.name, self.last_name)

my_student = Student("John", "Smith", "12345")

my_student.show_name()
print(my_student.student_id)
