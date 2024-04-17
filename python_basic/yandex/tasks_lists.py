# создать список из 5 разных типов элементов
lists = [1, '2', 2.3, True, 'Alex']
# Удаление 3 элемента из списка
lists.pop(3)
# выведите в терминал длину списка
print(len(lists))
# поменяйте порядок следования элементов в списке
lists.reverse()
print(lists)
# создайте еще один список с двумя элементами
new_lists = [9, 'Ivan']

joined_lists = lists + new_lists
print(joined_lists)

# for elemen in new_lists:
#    lists.append(elemen)
# print(lists)

lists.extend(new_lists)
print(lists)


first_list = [1, 2, 8, 4, False]
second_list = [3, 2, 4, True, 'Marlyn']
# another_list = first_list + second_list
another_list = first_list.__add__(second_list)
print(another_list)
