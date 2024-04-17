# область видимости определяет
# границы действия переменной
a = 10


def my_fn():
    a = True
    b = 15
    print(a)
    print(b)


my_fn()

print(a)
# print(b)  # name b is not defined

c = 3


def my_new_fn():
    def inner_fn():
        print(c)
    inner_fn()


my_new_fn()

# типы областей видимости
# глобальная область видимости
# область видимости функции


def another_my_fn():
    global k
    k = 31


another_my_fn()

print(k)
