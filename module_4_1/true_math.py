from math import inf


def divide(first, second):  # Функция divide, которая принимает два параметра first и second
    if second == 0:
        return inf
    else:
        return first / second
