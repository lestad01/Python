# список это упорядоченная изменяемая коллекция объектов разных типов
# my_list = []
# print(type(my_list))

# my_list_2 = list()
# print(type(my_list_2))



# print(len(my_list_3))

# срез
# print(my_list_3[:3])
my_list_3 = ["Выпить кофе", "Изучить Python", "Захватить мир", "Купить молоко"]

my_list_3.append("Купить билеты в театр")
# print(my_list_3)

my_list_3.insert(1, "Принять ванну")
print(my_list_3)

my_list_3.pop(-2)
print(my_list_3)

# удалится последний элемент
my_list_3.pop()
print(my_list_3)

# соединяет 2 списка в один
list2 = ["Пожарить мясо", "Сходить в бассейн", "Пожарить мясо"]
my_list_3.extend(list2)
print(my_list_3)

# удаление элемента с переданным значением

my_list_3.remove("Пожарить мясо")
print(my_list_3)
# если в списке есть несколько элементов с одинаковым значением
# удалит только первый элемент


new_list = my_list_3.copy()
print(new_list)

print(new_list.count("Пожарить мясо"))

print(new_list.index("Пожарить мясо"))

# print(new_list)
# new_list.sort()
# print(new_list)


n_list = [22, 13, 11, 41, 8]
# n_list.sort()
# n_list.reverse()
# print(n_list)

print(min(n_list))
print(max(n_list))

words_list = ["за", "тобой", "выехали"]
# new_str = "".join(words_list)
new_str = " ".join(words_list)
# new_str = ".".join(words_list)
print(new_str)

words_list.clear()
print(words_list)
