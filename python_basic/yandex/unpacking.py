# распаковка - извлечение значений и присвоение их переменным
# list, tuple - упорядоченные последовательности элементов
# распаковка списков LIST
my_fruits = ['apple', 'banana', 'lime']
my_apple, my_banana, my_lime = my_fruits

print(my_apple)
print(my_banana)
print(my_lime)
# ------------------------
# аналогичная ситуация с кортежами TUPLE
# в кортеж нельзя добавлять новые элементы


# оператор * при распаковке
# my_apple, *remaining_fruits = my_fruits

# print(my_apple)
# print(remaining_fruits)

# распаковка словаря в аргументы с ключевыми словами
# user_profile = {
#    'name': 'Alex',
#    'comments_qty': 23
# }

user_data = ['Aleksander', 28]


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


my_name, my_comments_qty = user_data
# print(user_info(**user_profile))

# print(user_info(name=user_data[0], comments_qty=user_data[1]))  именнованные аргументы
print(user_info(my_name, my_comments_qty))
print(user_info(*user_data))
