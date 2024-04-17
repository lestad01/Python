# унарные операторы всегда имеют один операнд
# my_num = 10
# print(+ my_num)

# my_bool = False
# print(+my_bool)
# my_num = 1
# print(not my_num)


# бинарные операторы
# у бинарных операторов два операнда
# a = 5
# a + b
# a += 5
# a == b
# a and b

# инфиксная запись
# когда оператор находится м/у операндами
# a = True
# a + b

# --------------------
my_car = {
    'brand': 'Toyota',
    'price': 10_000
}

# print('brand' in my_car)
# print('year' in my_car)
# print('year' not in my_car)

# приоритетность операторов

j = {1, 'Sashko', 3}
i = {3, 'Sashko', 1}

print(j == i)  # одинаковые значения переменных в наборах
print(j.__eq__(i))


print(j is i)   # разные объекты, но не значения объектов
print(0 not in j)
