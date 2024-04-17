# бинарный поиск
def binary_search(list, item):
    # начальное значение массива
    low = 0
    # последнее значение массива
    high = len(list) - 1
    # print(high)
    # проверяем средний элемент массива
    while low <= high:
        # середина массива
        mid = round((low + high)/2)
        print('Mid ' + str(mid))
        # находим середину/ среднее значение массива
        guess = list[mid]
        print('Guess ' + str(guess))
        # print(guess)
        if guess == item:
            return 'Индекс значения параметра: '.__add__(str(mid))
        # много
        if guess > item:
            high = mid - 1
            print('High ' + str(high))
        # мало
        else:
            low = mid + 1
            print(print('Low ' + str(low)))
    return None


my_list = [1, 2, 3, 18, 19, 25]
print(binary_search(my_list, 18))


# имеется отсортированный список из 128 имен , и вы ищете в нем значение
# методом бинарного поиска.
# Какое максимальное количество проверок для этого мб ?
# 128 -> log 128 == 7   .
# print(pow(2, 7)) -> 7 проверок

# предположим , размер списка
# увеличился вдвое. Как изменится
# максимальное количество првоерок?
# 256  увеличится на 1 проверку т.е. проверок макс
# будет 8
