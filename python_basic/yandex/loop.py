# for in для словарей и метод items()

my_object = {
    'x': 10,
    'y': True
}

for item in my_object.items():
    print(type(item))
    key, value = item
    # print(type(key))
    # print(type(value))

# for in для наборов (SET)
videos_ids = {1422, 1121, 3213, 5530}

for id in videos_ids:
    print(id)

# for RANGE диапазанов

for num in range(4, 12, 2):
    print(num)
