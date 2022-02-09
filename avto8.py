import itertools


def d(x):
    u = ''
    for i in x:
        u += i
    return u


def programm(nabor, first):
    """
    :param nabor: используемый алфавит
    :param first: искомый набор
    :return: номер набора
    """
    t = list(map(d, list(itertools.product(nabor, repeat=len(first)))))
    return t.index(first) + 1


print(programm("аоу", "уауау"))
