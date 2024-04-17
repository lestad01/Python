# Создайте функцию, которая будет
# конвертировать словарь в список кортежей
dict_main = {1: 'Csq23G', 2: True, 3: 'F3$sqs', 4: 3}


def dict_to_list(dict_to_convert):
    list_for_convertion = []
    # return list(dict_to_convert.items())
    for k, v in dict_to_convert.items():
        if type(v) == int:
            v *= 2
        list_for_convertion.append((k, v))
    return list_for_convertion


print(dict_to_list(dict_main))

# создайте функцию filter_list которая
# будет фильтровать список

obj = [35, True, 'Abc', 11]


def filter_list(list_to_filter, value_type):
    filtered_list = []
    for item in list_to_filter:
        # Не рекомендуется. Поскольку bool является субклассом класса числа
        # if isinstance(item, value_type):
        if type(item) == value_type:
            filtered_list.append(item)
    return filtered_list


print(filter_list(obj, int))

# func filter


def filter_list_new(list_filt, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)

    # return list(filter(check_element_type, list_filt))
    return list(filter(lambda elem: type(elem) is value_type, list_filt))


result = filter_list_new([1, 10, 'abc', 5.7], str)
print(result)
