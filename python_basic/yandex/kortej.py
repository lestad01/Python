# Кортежи
# упорядоченная последовательность элементов
# менять кортежи нельзя type tuple
# кортеж , как правило, небольшие в них 3-5 элемнта
my_fruits = ('banana', 'apple', 'lime')
# в разных кортежах разная упорядоченность кортеж не будет равен другому кортежу
my_new_fruits_list = ('banana', 'lime', 'apple')

print(my_fruits == my_new_fruits_list)
# -----------
posts_id = (122, 212, 84, 37)
print(posts_id[2])
# для получения последнего значения ID из кортежа
print(posts_id[-1])


# кортеж словарей МОЖЕМ МЕНЯТЬ
users = (
    {
        'user_id': 23,
        'user_name': 'Alex'
    },
    {
        'user_id': 11,
        'user_name': 'Misha'
    }
)

print(users[1]['user_id'])

# меняем значение ключа словаря
users[1]['user_id'] = 6
print('новое значение: ', users[1]['user_id'])
print(users[1])
# ------------------

internal_id = (11, 21, 74, 87)
external_id = (74, 75, 93, 11)
# используем магич. метод __add__ *
# для объединения кортежей
all_ids = internal_id + external_id
print(all_ids)

# методы кортежей , их два:
# методы кортежей наследуются от класса tuple
# count
print(all_ids.count(11))
# index
# если элемент встречается
# несколько раз , то возвращается индекс 1 элемента
pos_id = (5, 2, 3, 8, 3, 1)
print(pos_id.index(3))
print(pos_id.index(2))
# конвертация кортежа в список
new_pos_id = list(pos_id)
new_pos_id.append(228)
print(new_pos_id)
new_pos_id_tuple = tuple(new_pos_id)
print(new_pos_id_tuple)


my_tuple = tuple({'first': 1, 'second': True})
print(my_tuple)
