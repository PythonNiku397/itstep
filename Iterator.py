#my_list = [1,2,3]
# iterator = iter(my_list)
# print(iterator)
# print(next(iterator))

# numbers = [1, 2, 3, 4, 5]
# iterator = iter(numbers)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))
#
# for num in iterator:
#     print(num)
# for num in iterator:
#     print(num)

# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def next (self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(5)
# # for elem in count:
# #   print(elem)
#
# print(count.__next__())
# print(count.__iter__())
# print(next(count))
# print(iter(count))
# print(next(count))

# def numere_pare(maxim):
#     numar = 0
#     while numar < maxim:
#         yield numar
#         numar +=2
# for numar in numere_pare(10):
#     print(numar)

# def generator():
#     yield 1
#     yield 2
#     yield 3
# gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def raise_to_the_degrees(number, max_degree):
#     i=0
#     for A in range(max_degree):
#         yield number**i
#         i+=1
# res = raise_to_the_degrees(122345, 10)
# print(res)
# for A in res:
#     print(A)

# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"I will help you with your {self.work}. Afterwards I will help you with {work}"
# helper = Helper("homework")
# print(helper("cleaning"))
# def helper(work):
#     work_in_memory = work
#     def asd(work):
#         return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
#     return asd
# helper = helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))

def checker(function, *args, **kwargs):
    try:
        result = function(*args, **kwargs)
    except Exception as exc:
        print(f"We have problems {exc}")
    else:
        print(f"No problems. Result - {result}")
def calculate(expression):
    return eval(expression)
checker(calculate, "2+2")