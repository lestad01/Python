# Структуры данных, изменяемость
# это какой то тип данных который может заключать в себе др тип данных

# кортежи - tuple
# print(type((int,float)))


numbers = (1,2,3,7,9)
# print(numbers)


words = ("hello", "world", "number")
# print(words)


tuple_of_any = (1,2,3,"one", "four", False)
# print(tuple_of_any)


tuple_of_tuples = (numbers, words,tuple_of_any)

# в кортежах данные упорядочены
# print(tuple_of_tuples)


# print(len(numbers))
# print(numbers[2:4])

# numbers[:]
# print(numbers)

# print(numbers == numbers[:])

# word = words[0]
# print(word[1:2])

print(tuple_of_tuples[1])

print(tuple_of_tuples[2][4])
