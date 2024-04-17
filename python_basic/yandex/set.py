# set - неупорядоченная последовательность
# элементов
# набор содержит только
# уникальные элементы
# можно изменять наборы и удалять

# my_fruits = {'apple', 'banana', 'lime'}
# print(my_fruits)

# print(type(my_fruits))
# <class 'set'> экземлпяр класса set

# posts_id = {151, 211, 167, 151, 211}
# print(posts_id)

# print(type(posts_id))

# other_fruits = {'apple', 'lime', 'banana'}
# print(other_fruits == my_fruits)

# print(len(posts_id))
# индексо у элементов в наборе нет


# posts_ids = {10, 22, 13}

# posts_ids[1]


# изменяемые элементы в наборах не могут
# присутствовать
# lists_set = {[1, 2], [21, 16]}
# удалять элементы с помощью del нельзя
my_set = {10, 10, 4, 15, 15}
print(my_set)
print(len(my_set))

# пустой набор
my_new_set = set()
print(my_new_set)


# методы наборов
# методы наборов наследуются от класса SET

photo_sizes = {'1920x1080', '800x600'}

# добавление значения в набор
photo_sizes.add('1024x768')
print(photo_sizes)

# union или | метод объединения значений наборов
other_sizes = {'1024x768', '1920x1080'}
# all_sizes = photo_sizes.union(other_sizes)
all_sizes = photo_sizes.union(other_sizes)
print(all_sizes)

# intersection или & находит элементы набора
# которые находятся в двух элементах
common_s = other_sizes.intersection(photo_sizes)
print(common_s)

# issubset показывает включен ли один набор
# в другой набор
nums = {1, 10, 9, 21}
other_nums = {2, 13, 1, 10, 0, 9, 21}
res = nums.issubset(other_nums)
print(res)


my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}
# print(my_set.intersection(other_set))
print(my_set.intersection('abcd'))

print(my_set.union(other_set))
# множество other_set яне является подмножеством my_sets
print(other_set.issubset(my_set))

# difference показывает разницу между наборами
print(my_set.difference(other_set))
# удаляет элемент из набора
print(my_set.discard('d'))
print(my_set)

copied_set = my_set.copy()
print(copied_set)
print(my_set & copied_set)
