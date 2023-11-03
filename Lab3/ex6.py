def ex6(lst):
    unique = set(lst)
    return (len(unique), len(lst) - len(unique))


if __name__ == '__main__':
    print(ex6([1, 2, 2, 3, 4, 4, 5]))