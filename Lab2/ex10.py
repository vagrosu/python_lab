def ex10(*lists):
    tuples = []
    max_len = max(len(lst) for lst in lists)
    for item in lists:
        for i in range(max_len):
            if i >= len(tuples):
                if i < len(item):
                    tuples.append((item[i],))
                else:
                    tuples.append((None,))
            else:
                if i < len(item):
                    tuples[i] += (item[i],)
                else:
                    tuples[i] += (None,)

    return tuples


if __name__ == '__main__':
    print(ex10([1, 2, 3], [5, 6, 7, 8], ["a", "b", "c", "d"]))
