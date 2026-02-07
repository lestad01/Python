from itertools import (
    zip_longest,
    cycle,
    chain,
    count,
    combinations,
    combinations_with_replacement,
    permutations,
    repeat
)

names = ["Sam", "Nick", "Jake", "James"]
names_female = ["Ann", "Kate"]
surnames = ["white", "Black", "Smith", "Bond"]
emails = ["a@b.com", "name@example.com", "lestad01@mail.ru",]

all_names = names + names_female
names_male_and_female = [names, names_female]


def demo_zip():
    pairs = zip(names, surnames)
    print(list(pairs))

    names_pairs = [('Sam', 'White'), ('Nick', 'Black'), ('Jake', 'Smith')]
    result = list(zip(*names_pairs))
    print(result)

    result_3 = zip(names, surnames, emails)
    print(list(result_3))

# zip берет минимальное колличество элементов в списках
    source = [('Sam', 'white', 'a@b.com'), ('Nick', 'Black', 'name@example.com'), ('Jake', 'smith', 'lestad01@mail.ru')]
    result_2 = list(zip(*source))
    print(result_2)

def demo_zip_longest():
    collection = list(zip_longest(names, surnames, emails, fillvalue=""))
    print(collection)

def demo_cycle():
    email_demo = ["a@b.com", "c@d.com"]
    c = cycle(email_demo)
    pairs = zip(names, c)
    #pairs = zip(names, cycle(email_demo))
    print(list(pairs))

    #pairs = zip(surnames, cycle(email_demo))
    pairs = zip(surnames, c)
    print(list(pairs))
# chain выпрямляет в один список все элементы
def demo_chain():
    print(names_male_and_female)
    print(list(chain(*names_male_and_female)))
    print(list(chain(names, names_female, surnames, emails)))

def demo_count():
    c = count()
    # c = count(10, step=10)
    # print(c)
    # print(c)
    # print(next(c))
    # print(next(c))
    # print(c)
    result = zip (chain.from_iterable(names_male_and_female),c, )
    print(list(result))

def demo_combinations():
    nums = list(range(3))
    print(nums)
    print(list(combinations(nums, 2)))

    print(list(combinations(names, 3)))

def demo_combinatios_with_rp():
    print(list(combinations_with_replacement(range(3), 2)))
    print(list(combinations_with_replacement(names_female, 3)))

def demo_permutations():
    print(list(permutations(names, 2)))

def demo_repeat():
    c = cycle([3])
    print(list(map(pow, range(5), c)))
    print(c)

    r = repeat(2)
    print(list(map(pow, range(5), r)))
    print(r)

def main():
    #demo_zip()
    #demo_zip_longest()
    #demo_cycle()
    #demo_count()
    #demo_combinations()
    #demo_combinatios_with_rp()
    #demo_permutations()
    demo_repeat()

if __name__ == '__main__':
    main()