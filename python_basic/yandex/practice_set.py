my_num = {11, 8, 11, 7, 0}
print(my_num)

my_num.add(1224)
print(my_num)

new_set = {11, 8, 2, 4, 0}
union_set = my_num.intersection(new_set)
print(union_set)

new_set_2 = list(union_set)
print(new_set_2)
