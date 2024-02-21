# print("Hello")
# print("Hello")
# print("Hello")
#
# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         print("I am alive!")
#
# first_student = Student()
# first_student = print(first_student.height)

# class Student:
#     def __init__(self, height=160):
#         self.height = height
#
# nick = Student()
# kate = Student(height=170)
# Chiril = Student(height=2033)
# print(nick.height)
# print(kate.height)
# print(Chiril.height)

class Student():
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students+=1

nick = Student()
kate = Student(height=170)
chiril = Student()
print(nick.amount_of_students)
print(Student.amount_of_students)