import operator
from functools import reduce


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

def main():
    demo_reduce()

if __name__ == '__main__':
    main()