"""
    'I' - открывает файл на чтение. (Значение по умолчанию)
    'W' - открывает файл на запись. Если файла нет, то будет создан новый. Перезаписывает все что было в файле.
    'X' - открывает файл на запись. Если файл уже существует операция завершится с ошибкой.
    Создает новый файл , если он не существует.
    't' - Открывает файл как текстовый. (значение по умолчанию)
    'b' - открывает файл в бинарном/двоичном режиме.
    '+' - позволяет работать с файлом как для записи так и для чтения.
    'a' - для добавления данных в файл 
""" 
# encoding = 'cp1251'

# file = open(file = 'requires.txt', mode='r+', encoding='utf-8') 
# print(file.name)
# print(file.mode)
# print(file.read())
# file.close()

#with open(file='requires.txt') as new_file:
    #print(new_file.read())
    #print(new_file.readline())
    #print(new_file.readlines())

    # for line in new_file.readlines():
    #     print(line.strip())
    # for line in new_file:
    #     print(line.strip())


# my_str = 'Hack The Planet'
# new_str = 2
# password = ['qwerty', '123112', 'I am Grut']

# with open(file='secret_file.txt', mode='a') as file:
    #file.write(str(my_str))

    # for pas in password:
    #     file.write(f'{pas}\n')

import requests

response = requests.get(url='https://img2.akspic.ru/crops/0/8/7/7/7/177780/177780-chelovek_pauk-klyuch_cvetnosti-majlz_morales-supergeroj-komiksy-3840x2160.jpg')

with open(file='new_img.jpg', mode='wb') as file:
    file.write(response.content)