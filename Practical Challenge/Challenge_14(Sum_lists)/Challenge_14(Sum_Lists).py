from random import randint


def list_append() -> list:
    '''
    Creates a randomized listof numbers in range of 10.
    :return: list of integer numbers
    '''
    list = []
    for n in range(1, 11):
        number = randint(1, 10)
        list.append(number)
    return list


def united() -> list:
    '''
    Unify the two lists into a new list
    :return: Both lists combined into a new one.
    '''
    total = zip(list_a, list_b)
    list_total = list(total)
    return list_total


def list_sum() -> list:
    '''
    Using list comprehension we are summing both values of each list
    :return: new list containing the zipped list values summed.
    '''
    total_sum = [(v1 + v2) for v1, v2 in united()]
    return total_sum


list_a = list_append()

list_b = list_append()


if __name__ == '__main__':
    print(united())
    print()
    print(list_sum())
