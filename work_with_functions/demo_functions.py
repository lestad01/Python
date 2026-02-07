import operator
from functools import reduce, lru_cache, partial


def mul(a, b):
    print("a =", a, "b =", b)
    return a * b


def demo_reduce():
    # упрощенная форма
    print(sum(range(10)))
    # по сложнее форма
    # result = reduce(lambda a, b: a + b,range(5))
    # print(result)

    # result = reduce(lambda a,b: a * b, [2,3,4,5])
    #print(result)

    # result1 = reduce(mul, [2,3,4,5])
    # print(result1)

    result1 = reduce(operator.mul, [2, 3, 4, 5])
    print(result1)

    line = reduce(operator.concat, ["abc", "def", "ggi"])
    print(line)
    line = "".join(["abc", "def", "ggi"])
    print(line)


def demo_reduce_pro():
    print(min(1,2))
    print(max(1,2))

    numbers = (2, 3, 4, 0, 7)
    print(reduce(min, numbers))
    print(reduce(max, numbers))

# декораторы. Оборачиваем при помощи декоратора в кэш данную функцию.
# (maxsize=None) - кеш не ограничен
# Хорошо подходит для:
# Рекурсивных функций.
# Функций, которые часто вызываются с одинаковыми аргументами.
# Функций с дорогими вычислениями.
@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

#print(fib(5))

def demo_fib():
    print(list(map(fib, range(109))))

def demo_partial():
    mul_2 = partial(mul, 2)
    print(mul_2(3))

    mul_3 = partial(mul, 3)
    print(mul_3(4))

    square = partial(pow, exp = 2)
    print(square(3))
    print(square(4))


def main():
    # demo_reduce()
    # demo_fib()
    # demo_partial()
    demo_reduce_pro()


if __name__ == '__main__':
    main()