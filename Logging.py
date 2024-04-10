# import logging
# # logging.basicConfig(level=logging.DEBUG)
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
#
# import logging
# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w")
# logging.info("info")
# logging.debug("debug")

# import logging
# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="We have next logging message:%(asctime)s:%(levelname)s -%(message)s")
# logging.info("info")
# logging.debug("debug")

# if 2+2==4:
#     print("It's real!")
# assert 2+2==5, "It's Fake"

# def divide(a, b):
#     assert b != 0, "Division by zero is not allowed"
#     return a / b
# print(divide(10, 2))
# print(divide(10, 0))

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