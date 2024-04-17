# функция - блок кода
# который можно выполнять многократно
def sum(a, b):
    c = a + b
    print(c)


print(type(sum))

# каждая функция - это
# экземпляр класса function

# функция возвращает NONE
# если нет ключевого слова
# RETURN

# name = input("Enter your name: ")
# print(name)


# функция dir

# name = 'Alex'
# print(dir(name))
# print(name.upper())


# print(dir(__builtins__))

# функция input

# name = input("Enter your name: ")


# print(name.capitalize())


# самая короткая функция pass
def my_func():
    pass  # ключевое слово используется когда функция нужно не знаем для чего


print(my_func())


# передача неизменяемых объектов
# в функцию
def my_fn(a, b):
    a = a + 1
    c = a + b
    return c


num_one = 10
num_two = 2

res = my_fn(num_one, num_two)
print(res)
print(num_one)

# передача изменяемых объектов
# в функцию

# изменяем внешний объект


# def increace_person_age(person):
#    person['age'] += 1
#    return person


# person_one = {
#    'name': 'Bob',
#    'age': 22
# }

# increace_person_age(person_one)
# print(person_one['age'])

# внутри функции не рекомендуется изменять
# внешние объекты

# как избегать изменения
# внешних объектов в функции
def increace_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Bob',
    'age': 22
}

new_person = increace_person_age(person_one)
print(new_person['age'])
print(person_one['age'])


# Задачка
def merge_lists_to_dict(first_list, second_list):
    new_list = dict(zip(first_list, second_list))
    return new_list


print(merge_lists_to_dict([1, 2, 0, 11], [True, 'Charlie', '86', 'Alex']))


# def sum_nums(*args):
# print(args)
# print(type(args))
# print(args[0])
# return sum(*args)


# print(sum_nums(0))


# def get_posts_info(name, posts_qnty):
#    info = f"{name} wrote {posts_qnty} posts"
#    return info


# позиционные аргументы. порядок аргументов важен
# info = get_posts_info('Alex', 23)
# print(info)

# -----------------------------------------

# def get_posts_info(name, posts_qnty):
#    info = f"{name} wrote {posts_qnty} posts"
#    return info


# аргументы с ключевыми словами. Порядок аргументов не важен
# info = get_posts_info(name='Alex', posts_qnty=23)
# print(info)


# объединение аргументов в DICT словарь
def gets_post_info(**person):
    print(person)
    print(type(person))
    info = {
        # если не ставить запятую Python объединяет две строки
        f"{person['name']} wrote "
        f"{person['posts_qnty']} posts"
    }
    return info


info = gets_post_info(name='Alex', posts_qnty=11, id=1352)
print(info)


# значения параметров функции по умолчанию
def mult_by_factor(value, multiplier=1):
    return value * multiplier


print(mult_by_factor(10, 2))
print(mult_by_factor(5))
