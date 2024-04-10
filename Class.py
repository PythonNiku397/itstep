# class Human:
#     height = 170
# class Student(Human):
#     pass
# class Worker(Human):
#     pass
# nick = Student()
# ann = Worker()
# print(nick.height)
# print(ann.height)
#
# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
# class Parent(Grandparent):
#     age = 40
# class Child(Parent):
#     height = 50
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
# nick = Child()
#
# class Hello_world:
#     hello = "a"
#     _hello = "b"
#     __hello = "c"
#     def __init__(self):
#         self.world = "1"
#         self._world = "2"
#         self.__world = "3"
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
# class Hi(Hello_world):
#     def hi_print(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
# hello = Hello_world()
# hi = Hi()
# hi.hi_print()

# class Hello:
#     def __init__(self):
#         print("Hello!")
# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World!")
# hello_world = Hello_World()

# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
# hello_world = Class2()
#
class Grandparent:
    def about(self):
        print("I am GrandParent")
    def about_myself(self):
        print("I am GrandParent")
class Parent(Grandparent):
    def about_myself(self):
        print("I am a Parent")
class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()
nick = Child()
#
# class Computer:
#     def __init__(self):
#         super().__init__()
#         self.memory = 128
# class Display:
#     def __init__(self):
#         super().__init__()
#         self.resolution = "4k"
# class SmartPhone(Display, Computer):
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)
# iphone = SmartPhone()
# iphone.print_info()

# class Computer:
#     def __init__(self, model, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.model = model
#         self.memory = 128
# class Display:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.resolution = "4k"
# class SmartPhone(Display, Computer):
#     def print_info(self):
#         print(self.model)
#         print(self.resolution)
#         print(self.memory)
# iphone = SmartPhone(model = "Last")
# iphone.print_info()