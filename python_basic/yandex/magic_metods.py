# Магические методы - это внутренние методы классов
# и они обычно не вызываются явно
print(bool)
print(dir(bool))

# __doc__ показывает что делает функция str
print(bool.__doc__)

# помощь о каждом методе
my_list = []
print(help(list.__eq__))
print(help(my_list.__eq__))

a = [1, 2]
b = [1, 2]

print(a is b)
print(a == b)
print(a.__eq__(b))
print(a.__eq__)
