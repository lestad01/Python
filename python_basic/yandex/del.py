my_dict = {'a': True, 'b': 10}

del my_dict['a']
my_dict.__delitem__('b')

print(my_dict)


my_list = [1,2]

print(del my_list[0]) # инструкциря так же как и с return
