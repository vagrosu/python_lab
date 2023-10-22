def ex11(lst):
    return sorted(lst, key=lambda tup: tup[1][2])


if __name__ == '__main__':
    print(ex11([('abc', 'bcd'), ('abc', 'zza')]))