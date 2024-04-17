# (range) - диапазон упорядоченная
# неизменяемая последовательность элементов
# обычно используются в циклах
my_range = range(7)  # передаем экземпляр класса range
print(my_range)
print(type(my_range))
print(list(my_range))

my_new_range = range(10, 20, 2)
for i in my_new_range:
    print(i)


print(list(my_new_range))
