# методы списков
# все методы списков объекты наследуют класс LIST
happy_smiles = []
happy_smiles.append("23")
happy_smiles.append(9)

print(happy_smiles)

# pop удаление элемента из списка, когда используем
# без аргумента данный метож последний
lists = [1, 'true', False, 11, 'Alex']
lists.pop()
lists.pop(2)

print(lists)

# метод сортировки - sort
new_lists = [1, 0, 12, 32, 8]
new_lists.sort()
print(new_lists)

# по убыванию сортировки, используем с аргументом reverse = True
new_lists.sort(reverse=True)
print(new_lists)


# Конвертация в список
greeting = "Hello from Russia!"
greeting_lettels = list(greeting)

print(greeting_lettels)

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)
print(my_dict_keys)


ratings = [0.23, 22, 1, 33, 0.11]
print(min(ratings))
print(max(ratings))
print(sum(ratings))
print(round(sum(ratings) / len(ratings)))

my_ratings = [1.22, 12, 23, 0.18]
other_ratings = [2.12, 33, 17, 0.41]
all_ratings = my_ratings + other_ratings
print(all_ratings)

# Нарезка списков
new_list2 = my_ratings[1:-1]
print(new_list2)
