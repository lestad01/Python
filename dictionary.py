# словарь это не изменяемый не упорядоченная структура данных, которые хранят пары ключ - значение

# my_dict = {}
# my_dict2 = dict()

# print(type(my_dict))
# print(type(my_dict2))


# my_dict = {
#     "user": "Thosma Shelby",
#     "nickname": "Brivar",
#     "team": "Russia"
# }

# print(my_dict["user"])
# person = {1: "Виктор", 2: "Чернов", 3: "Сергеевич"}
# print(person[1])

# person["вес"] = 90
# print(person)

# del person["вес"]
# print(person)

# for key,value in person.items():
#     print(f"{key} >>>> {value}")

# for key in person.keys():
#     print(key)

# for key in person:
#     print(key)

# if 1 in person.keys():
#     print("Данный ключ уже используется")
# else:
#     print("Вы можете использовать данный ключ для создания пары")

# for value in person.values():
#     print(value)


# man = {
#     'name': 'Alex',
#     'age': 29,
#     'height': 181,
#     'weight': 91,
#     'main dish': ['карбонара', 'пельмени', 'картошка'],
#     'car': 'Audi'
# }

# for values in man['main dish']:
#     print(values)

persons = {
    'Alex': {
        'age': 29,
        'height': 181,
        'weight': 91,
        'main dish': ['карбонара', 'пельмени', 'картошка'],
        'car': 'Audi'
    },
    'Misha': {
        'age': 29,
        'height': 180,
        'weight': 85,
        'main dish': ['спегети', 'бургер', 'пицца'],
        'car': 'Hyundai'
    },
}


# for username, userinfo in persons.items():
#     print(f"Имя пользователя: {username}")
#     age = userinfo["age"]
#     car = userinfo["car"]

#     print(f"Возраст пользователя {username} : {age} лет. ")
#     print(f"Автомобиль пользователя {username} : {car}\n")


# print(persons)
# print(persons.get("Misha"))

# print(persons.setdefault("Kirill", "magic"))
# print(persons)


# person_copy = persons.copy()
# print(person_copy)

# persons.update({"профессия": "слесарь"})
# print(persons)

# print(persons.popitem())
# print(persons.popitem())
# print(persons.popitem())

print(persons.keys())
print(persons.values())
print(persons.items())

persons.clear()
print(persons)
