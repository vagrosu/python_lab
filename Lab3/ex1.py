def ex1(a, b):
    sets = [set(), set(), set(), set()]
    sets[0] = set(a) & set(b)
    sets[1] = set(a) | set(b)
    sets[2] = set(a) - set(b)
    sets[3] = set(b) - set(a)
    return sets


if __name__ == '__main__':
    print(ex1([1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 8]))
