
my_number = 25

if my_number > 0:
    print(my_number, "is positive number")


person_info = {
    'age': 20
}

if not person_info.get('name'):
    print("Имя отсутствует")

if 10 > 2:
    print(True)


my_phone = {
    'price': 200,
    'brand': 'Iphone',
}

if my_phone.get('brand'):
    print("Phone's brand is", my_phone['brand'])
else:
    print("There is no phone brand")


# ----------------------------------------------
my_new_number = -5

if my_new_number > 0:
    print(my_new_number, "is positive number")
elif my_new_number < 0:
    print(my_new_number, "is negative number")
else:
    print(my_new_number, "is zero")


# ------------------------------------------------
# Задачка

def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your destination is {route['distance']}"
    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * route['time']}"
    return "No distance info is available"


print(route_info({'distance': '15'}))
print(route_info({'speed': 15, 'time': 2}))
print(route_info({'our_speed': 35}))


# Тернарный оператор
print("is int") if type(my_new_number) is int else print("is not int")

my_img = ('1920', '1080')

print(f"{my_img[0]}x{my_img[1]}") if len(
    my_img) == 2 else "Incorret image formatting"
# print(info)
