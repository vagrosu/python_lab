def ex3(a, b):
    intersection = [val for val in a if val in b]
    reunion = a + [val for val in a if val in b]
    dif1 = [val for val in a if val not in b]
    dif2 = [val for val in b if val not in a]

    return intersection, reunion, dif1, dif2


if __name__ == '__main__':
    list1 = ["1", "2", "5", "10", "20", "30"]
    list2 = ["1", "2", "15", "100", "20", "300"]
    print(ex3(list1, list2))