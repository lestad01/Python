# input_str = input('Enter keyword: ')
# input_int = int(input_str)

# print(input_int)

# print(type(input_int))


# pow_number = pow(2, 3)
# print(pow_number)
# print(type(pow_number))


long_int = 1_000_000_000

print(long_int)

bool_val = True
int_value = 10

print(bool_val + int_value)

# магические методы

int_num = 50
float_num = 7.5
str_val = 'abc'

# print(str_val * int_num)

print(int_num.__mul__(str_val))
# NotImplemented

print(str_val.__rmul__(int_num))

# print(int_num + float_num)

# print(int_num.__mul__(float_num))
# NotImplemented

# print(float_num.__rmul__(int_num))
