# копирование списка
my_cars = ['BMV', 'Mercedes']

# копирование по ссылке
# не желательный метод копирования
copied_cars = my_cars

copied_cars.append('Ford')

print(copied_cars)


print(id(my_cars) == id(copied_cars))


# верный метод копирования
# 1 вариант [:] - создает новый объект
new_copied_cars = my_cars[:]
new_copied_cars.append('Audi')

print(id(my_cars) == id(new_copied_cars))


# 2 вариант метод списков copy
another_copied_cars = my_cars.copy()
another_copied_cars.append('Folkswagen')

print(id(my_cars) == id(another_copied_cars))


# 3 вариант list создает новый список
copy_cars = my_cars.copy()
copy_cars.append('Audi')

print(id(my_cars) == id(copy_cars))


my_nums = [1, 1, 6, 3, 21]
print(my_nums.count(21))


my_nums.insert(2, -9)
print(my_nums)

my_nums.extend('123')
print(my_nums)

my_nums.clear()
print(my_nums)
