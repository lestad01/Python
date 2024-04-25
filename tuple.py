# кортежи не изменяемы упорядоченные объекты не можем удалять изменять значения

# tuple = (1,2,3)
# print(tuple)

# my_tuple = 1,
# print(type(my_tuple))


# my_list = ["python", "is", "awesome"]
# my_typle = ("python", "is", "awesome")

# print(my_list.__sizeof__())
# print(my_typle.__sizeof__())

# print(my_typle[0:1])

#print(len(my_typle))

# добавить удалить или ищзменить элемент в кортеже мы не можем


# my_typle = ("python", "is", "awesome")
# print(id(my_typle))

# my_list = list(my_typle)
# my_list.append("and so useful")
# print(my_list)

# my_typle = tuple(my_list)

# my_typle = (1,2,3) + my_typle
# print(my_typle)

my_tuple = ("python", "is", "awesome", [1, 2, 3], 88, ("a", "b", "c"))

print(my_tuple.index(88))
# print(my_tuple)
# print(id(my_tuple))

# my_tuple[3].append(21)
# print(my_tuple)

# print(my_tuple.count("python"))
# print(my_tuple.count(88))

del my_tuple
print(my_tuple)