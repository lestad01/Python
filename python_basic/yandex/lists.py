# список list - упорядоченная последовательность элементов
elements = [1, 22, 'true', False]
print(elements[3])

elements[3] = True
elements[2] = 'false'

print(elements[3])

# оператор del для удаление элемента из списка
del elements[2]

print(len(elements))

# Список словарей
users = [
    {
        'user_id': 12,
        'user_name': 'Alice'
    },
    {
        'user_id': 3,
        'user_name': 'Bob'
    }
]

print(len(users))
print(users[1]['user_name'])


my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'
all_fruits = [my_fruit, other_fruit, new_fruit]
print(all_fruits)
