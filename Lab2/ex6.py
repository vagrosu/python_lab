def ex6(*lists, x):
    frequency = {}
    for lst in lists:
        for items in lst:
            if items in frequency:
                frequency[items] += 1
            else:
                frequency[items] = 1

    for lst in lists:
        for items in lst:
            if frequency[items] != x:
                break
        else:
            return lst
    return []


if __name__ == '__main__':
    count = 2
    print(ex6([1, 2, 7], [2, 3, 4], [4, 5, 6], [5, 3, "test"], x=count))
