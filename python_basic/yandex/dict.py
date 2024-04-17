# словарь набор данных с типом ключ:значение
my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}
# порядок элементов в словаре не имеет значения
# индексо у элементов в словаре нет
other_motorbike = {
    'engine_vol': 1.2,
    'price': 25000,
    'brand': 'Ducati',
}
print(id(my_motorbike) == id(other_motorbike))
print(my_motorbike == other_motorbike)

my_motorbike['price'] = 6000
print(my_motorbike)

print(other_motorbike['brand'])
# print(other_motorbike[brand])
my_motorbike['is_new_key'] = True
print(my_motorbike)

del my_motorbike['is_new_key']
print(my_motorbike)

key_name = 'brand'
my_motorbike[key_name] = 'BMW'
print(my_motorbike)


new_other_motorbike = {
    'engine_vol': 1.6,
    'price': 15000,
    'brand': 'Audi',
    'price_info': {
        'price': 22000,
        'is_available': True,
    }
}

print(new_other_motorbike['price_info']['is_available'])

print('Длина списка: ', len(new_other_motorbike))

del new_other_motorbike['engine_vol']
print('Длина списка: ', len(new_other_motorbike))

# Метод словарей get
# данный метод нужен для получения значений ключей

print(new_other_motorbike.get('price'))
print(new_other_motorbike.get('model', 0))

my_dict = {}
# описание функции dict с  помощью которых можно создавать новые экземлпяры
#
print(my_dict.__doc__)
