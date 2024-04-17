# функция ZIP
fruits = ['apple', 'banana', 'lime', 'orange']
# quantaties = [100, 70, 50, 10]
quantaties = '2234'

availability = [True, False, False, True]


fruit_qtys_zip = zip(fruits, quantaties, availability)

print(fruit_qtys_zip)
# <zip object at 0x0000022AC2FB0340>
# код выше это локация объекта
# в памяти компьютера
print(type(fruit_qtys_zip))


fruit_qtys_zip = list(fruit_qtys_zip)

print(fruit_qtys_zip)
# при конвертации ZIP
# объекта в список получаем
# список кортежей

# конвертация ZIP в словарь DICT
vegetables = ['tomato', 'potato', 'onion']

new_quantaties = [10, 23, 17, 11]

vegetabl_qtys_zip = zip(vegetables, new_quantaties)
print(vegetabl_qtys_zip)
# <zip object at 0x00000178EA957CC0>

vegetabl_qtys_zip = dict(vegetabl_qtys_zip)
print(vegetabl_qtys_zip)
# при конвертации ZIP объекта
# в словарь dict допускается
# только 2 аргумента в вызове
# функции zip
# в первом аргументу указываются ключи
# во второй последовательности
