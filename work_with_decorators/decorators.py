from functools import wraps


def power_number(number, power=2):
    return  number ** power

number_and_power = (2,3)

#print(power_number(*number_and_power))

params_kwargs = {
    "power": 2,
    "number": 3,
}

#print(power_number(**params_kwargs))

# def power_numbers(*numbers, power = 2):
#     return [number ** power for number in numbers]

#print(power_numbers(3))

#print(power_numbers(*range(4)))

#print(power_numbers(*range(4), power=3))

# def my_function():
#     return print("My function runs")

# Декораторы в Python — это функции высшего порядка,
# которые позволяют модифицировать поведение других функций или методов, без изменения их кода.
#
# def my_decorator (func_to_decorate):
#     print("A. My decorator: create a new function")
#
#     def replacement_function():
#         print("B. running replacement function")
#         func_to_decorate()
#         print("C. finished running replacement function")
#         return func_to_decorate
#     print("D. created replacement function")
#     return replacement_function()

#my_function = my_decorator(my_function)

#result = my_function()
#print("Result: " , result)

# @my_decorator
# def small_func():
#     print("Im a small func")
#
# print(small_func())

# Декоратор @wraps(func) из модуля functools используется внутри других декораторов,
# чтобы сохранить метаданные оригинальной функции (например, __name__, __doc__, __module__ и т.д.).
# def my_dec(func):
#
#     @wraps(func)
#     def wrapper():
#         print("call func", func)
#         func()
#         print("finished wrapper")
#
#     return wrapper
#
# @my_dec
# def some_func():
#     print("some_func called")
#
# print(some_func())
# print(some_func.__wrapped__)


def dec_with_one_arg(func):
    @wraps(func)
    def wrapper(arg):
        print("call func", func, "with arg", arg)
        result = func(arg)
        print("-- result: ", result)
        return  result
    return  wrapper

@dec_with_one_arg
def cube (num):
    return num ** 3

print(cube(3))
#print(cube.__wrapped__)