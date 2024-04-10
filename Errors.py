# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except:
#     print("We have an error")
# print("code after capsule")

# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except NameError:
#     print("We have an NameError")
# print("code after capsule")

# try:
#     print("start code")
#     print(10/0)
#     print("No errors")
# except NameError:
#     print("We have an NameError")
# except ZeroDivisionError:
#     print("We have an ZeroDivisionError")

# try:
#     print("start code")
#     print(10/0)
#     print("No errors")
# except (NameError, ZeroDivisionError):
#     print("We have an Error")

# try:
#     print("start code")
#     print(10/0)
#     print("No errors")
# except (NameError, ZeroDivisionError) as error:
#     print(error)
# print("code after capsule")

# try:
#     try:
#         print("start code")
#         print(error)
#         print("No errors")
#     except SyntaxError:
#         print("Wrong Syntax")
# except NameError as error:
#     print(error)

# try:
#     print("Hello")
# except:
#     print("We have a problem")
# else:
#     print("No problem")

# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except NameError as error:
#     print(error)
# else:
#     print("l am ELSE!")
# finally:
#     print("Finally code")

# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"Sorry, we can't work with {type(var_1)}, " f"e=we need class str")
#     else:
#         return var_1
# first_var = "Hello"
# # first_var = 10
# checker(first_var)

# class BuildingError(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot be built!"
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "enough material"
#     else:
#         raise BuildingError(amount_of_material)
# materials = 123
# check_material(materials, 300)

# import warnings
# warnings.warn("warning, no code here", SyntaxWarning)