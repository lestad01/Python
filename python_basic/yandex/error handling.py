try:
    # Выполнение блока кода
    pass
except ErrorType:
    # Этот блок выполняется в случае
    # возникновения ошибок в блоке try
    pass

# try:
#    print(10 / 0)
# except ZeroDivisionError:
#    print("Error - Division by zero!")

# print('Continue...')

# -----------
# try:
#    print(2 / 0)
# except ZeroDivisionError as e:
#    print(type(e))
    # <class 'ZeroDivisionError'>
#    print(e)

# print('Another Continue...')


# другие типы ошибок

# try:
#    print('10' / 0)
    # Traceback - TypeError: unsupported
    # operand type(s) for /: 'str' and 'int'
# except ZeroDivisionError as e:
#    print(e)
# except TypeError as e:
#    print(type(e))
#    print(e)

# print('Continue...')


try:
    print(10 / 5)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:  # блок выполнится в случае если ошибок не возникло
    print("There was no error")
finally:  # данный блок выполнитлся в любом случае
    print('Continue...')

# любые ошибки в блоке except
try:
    print('10' / 0)
except Exception as e:
    print(e)

# OR

try:
    print(2 / 'qq')
except:
    print("Some error occured")
