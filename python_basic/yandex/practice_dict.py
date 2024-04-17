my_disk = {}

print(id(my_disk))
# экземлпяр класса dict
print(type(my_disk))


my_disk['price'] = 110
my_disk['brand'] = 'LG'

# print(my_disk)
# print(id(my_disk))

# print(my_disk.__doc__)

# вызывает спец объект класса dict items
print(my_disk.items())
print(type(my_disk.items()))

# print(my_disk.keys())

# удаляет последний ключ словаря
# print(my_disk.popitem())

# print(my_disk.get('type'))

# new_disk = my_disk.copy()

# new_disk['type'] = 'SSD'

# print(id(my_disk))
# print(id(new_disk))


# my_list = [['First', 0], ['Second', True], ['Third', 'ssd'], ['Fourght', 122]]

# my_new_dict = dict(my_list)
# print(my_new_dict)


# my_str = 'Alex, Andrey'
# my_dict = dict(my_str)

# print(my_dict)
