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

# class Student():
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=1
#
# nick = Student()
# kate = Student(height=170)
# chiril = Student()
# print(nick.amount_of_students)
# print(Student.amount_of_students)

# class Student:
#     height = 160
#     def __init__(self):
#         print(self.height)
#         self.height += 10
#
# nick = Student()
# kate = Student()

# class Student():
#     def __init__(self):
#         self.height = 170
#     height = 160
#
#     def printer(self):
#         print(self.height)
#
# nick = Student()
# nick.printer()

# x = 10
#
# class Locker:
#     print(x)
#     def func_1(self):
#         # x=20
#         print(x)
#         def func_2():
#             # x=30
#             print(x)
#
#         func_2()
# some_object = Locker()
# some_object.func_1()

# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=1
#     def grow(self, height=1):
#         self.height+=height
#
# nick = Student()
# kate = Student(height=170)
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)
# print(Student.amount_of_students)
# jora = Student()
# print(Student.amount_of_students)

# class Student():
#     def __init__(self, name=None):
#         self.name = name
#     def __str__(self):
#         return f"I am a student. My name is {self.name}."
#
# nick = Student(name = "Nick")
# print(nick)

# class Student:
#     def __init__(self, name=None):
#         self.name = name
#
#     def __str__(self):
#         if self.name:
#             return f"I am a student. My name is {self.name}."
#         else:
#             return f"I am a student. I don't have a name."
# alice = Student(name="Alice")
# print(alice)
# unknown_student = Student()
# print(unknown_student)
#
# import random
#
# class Student:
#
#     def __init__(self, name):
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.alive = True
#
#     def to_study(self):
#         print("Este timpul să învăț")
#         self.progress += 0.12
#         self.gladness -= 5
#     def to_sleep(self):
#         print("Voi dormi")
#         self.gladness += 3
#     def to_chill(self):
#         print("Timp de odihnă")
#         self.gladness += 5
#         self.progress -= 0.1
#     def is_alive(self):
#         if self.progress < -0.5:
#             print("DEAD...")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("Depresie...")
#             self.alive = False
#         elif self.progress > 5:
#             print("O murit de fericire...")
#             self.alive = False
#     def end_of_day(self):
#         print(f"Fericire = {self.gladness}")
#         print(f"Progres = {round(self.progress, 2)}")
#     def live(self, day):
#         day = " Ziua " + str(day) + " din viața lui " + self.name + " "
#         print(f"{day:=^50}")
#         live_cube = random.randint(1, 3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_of_day()
#         self.is_alive()
# nick = Student(name="Vlad")
# for day in range(365):
#     if nick.alive == False:
#         break
#     nick.live(day)

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result+=float(_)
                continue
            except(ValueError, TypeError):
                pass
            try:
                result+=int(_)
                continue
            except(ValueError, TypeError):
                pass
    for _ in kwargs.values():
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except(ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except(ValueError, TypeError):
                pass
    return result