"""
This is doc for this module
"""


# все в Питоне наследуется от Object
# можем создать новый экземпляр
some_object = object()
print(some_object)

long_string = """
Hello World!
"""

def my_func(a,b):
    ""
    """
    This is myfunc docstring

    This function swaps a and b
    """
    return a,b

help(my_func)
print(my_func(1,2))

# необходимо указывать pass означает тело и означает что ничего не делать
# то же самое и с пустой строкой
def hello():
    """
    this is hello doc

    """

print(hello.__doc__)
print(my_func.__doc__)
print(repr(my_func.__doc__))

# создаем новый класс
# int str ... наследуются от Object

# class User(object):
class User:
    """
    """

a = 1
b = ""
c = int()

user1 = User()

# создали новый тип на основе созданого типа. Кастомный объект
print(User)
print(user1)
print(type(user1))
print(User.mro())

user1.name = "Johny"
print("name:", user1.name)


# Есть проблемка если создадим user2 = User()
# у экземпляра user1 есть атрибут name, а user2 есть атрибут name и age
# у экземпляра user1 нет атрибута age
user2 = User()
user2.name = "Sam"
user2.age = 20
print("name:", user2.name)
#print("age:", user1.age)


print("user1 dict: ", user1.__dict__)
print("user2 dict: ", user2.__dict__)

# Создаем атрибуты для нового класса
