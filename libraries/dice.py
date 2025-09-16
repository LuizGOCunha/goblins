from random import randint


def d6() -> int:
    return randint(1, 6)


def d10() -> int:
    return randint(1, 10)


def d20() -> int:
    return randint(1, 20)


d_list = []
for _ in range(10000):
    d_list.append(d20())

print(set(d_list))
