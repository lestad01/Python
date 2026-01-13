##def hello():
##    print('hello world')

##print(hello())

##def hi(name):
##    print("Hello", name)

##hi(hi)

##def get_sum(a, b):
##   return a + b

##print(get_sum(1,5))
##print(get_sum('foo','bar'))

## позиционные и именованные аргументы 
##print(get_sum(a=3, b=4))

##def power_number(number, power):
##    return number ** power

##print(power_number(2, 3))

## именованный аргумент 
##print(power_number(power=4, number=2))
##print(power_number(4, power=3))

## позиционный аргумент
##def power_numbers(numbers, power=2):
##    results = []
##    for num in numbers:
##        results.append(num ** power)
##    return results

##print(power_numbers([1,2,3]))
##print(power_numbers([1,2,3], 3))

## еще пример именованного аргумента
##print(power_numbers([1,2,3], power=4))
##print(power_numbers(numbers=[1,3,5], power=3)) ## если один из аргументов указали именованным то второй тоже нужно указывать именованным

## короткая версия кода объявления функции
##def power_numbers(numbers, power=2):
##    return [num ** power for num in numbers]

##print(power_numbers(numbers=[1,2,3], power=4))

def power_numbers2(*numbers, power=2):
    return [num ** power for num in numbers]

##print(power_numbers2(2))
##print(power_numbers2(2,1,4,5,6))
##print(power_numbers2(21,3,2,1 , power=2))

##numbers = list(range(5))

##print(power_numbers2(numbers, 3))

odds = [num for num in range(10) if num % 2]
##print(odds)

##print(power_numbers2(*odds))

## списки упорядочены и изменяемы
## параметр со значением список не может быть по умолчанию
#def extend_list(new_data_seq, list_to_extend=[]):
##    for data in new_data_seq:
##        list_to_extend.append(data)
##    return list_to_extend
#print(extend_list([1,2],[0]))


#list1 = ['fizz']
#print(id(list1))

#list2 = extend_list(['buzz'], list1)
#print(list2)
#print(id(list2))
## если не передавать параметр изначально в функции extend_list в дальнейшем лист будет расширяться
#print(extend_list([1.5, 3.5]))


#print(extend_list([1,2], []))
## вот пример этого явления как расширяется лист
#print(extend_list([1,2]))

############################

##def extend_list_new(new_data_seq, list_to_extend=None):
##    if list_to_extend is None:
##        list_to_extend = []
##    for data in new_data_seq:
##        list_to_extend.append(data)
##    return list_to_extend

##print(extend_list_new([1,2,3]))

# значение по умолчаниюв функциях
#def find_by_key(key, **kwargs):
#    print('key:', key)
#    print('kwargs:', kwargs)

#print(find_by_key('spam', foo='bar', fizz='buzz'))

#def find_by_key(key, **kwargs):
#    if key in kwargs:
#        value = kwargs[key]
#        print('key:', key, 'found in kwargs, value = ', value)
#        return value
#    print('key:',key, 'not found')

#print(find_by_key('spam', foo='bar'))


#def find_by_key(key, **kwargs):
#    if key not in kwargs:
#        print('key:', key, 'not found')
#        return
#    value = kwargs[key]
#    print('key', key, 'found in kwargs, value =', value)
#    return value

#print(find_by_key('spam', spam = 'eggs'))

#def power_number(num, power=2):
#    return num ** power

#print(power_number(3, 4))

#print(list(map(power_number, [1,2,3,4])))

odds = [1, 3, 4, 5, 7, 9]
#print(list(map(power_number, odds, [3, 3, 3, 2, 2])))

# анонимные функции
#def square(n):
#    return n ** 2

#print(square(3))
#print(list(map(lambda num: num ** 2, odds)))

#print((lambda x: x ** 2)(3))

#print((lambda x, y: x ** y)(3, 3))

#print(list(filter(lambda x : True, range(10))))

evens = list(filter(lambda x: x % 2 == 0, range(10)))
print(evens)

def find_value(numbers):
    for number in numbers:
        if number == 0:
            continue
        if number % 3 == 0 and number % 5 == 0 :
            return "FizzBuzz", number
        if number % 3 == 0:
            return "Fizz", number
        if number % 5 == 0:
            return "Buzz", number

print(find_value([1, 2, 3, 6]))