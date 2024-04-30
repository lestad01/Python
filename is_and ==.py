# == 
# a == b

# is проверяет указывают ли перкеменныые на один и тот же объект в памяти
# a is b

# list_1 = [1,2,3]
# list_2 = [1,2,3]

# print(id(list_2))
# print(id(list_1))

# print(list_1 == list_2)

# print(list_1 is list_2)

# не изменяемые - 1,2,3 (1,2,3) True False
# изменяемые - ['a','b'] {'a','b,} {1:'123',2:'feq'}


my_str_1 = 'Hello Friend ss'
my_str_2 = 'Hello Friend'


print(id(my_str_1))
print(id(my_str_2))

print(my_str_1 == my_str_2)

print(my_str_1 is my_str_2)
