def ex7(*sets):
    res = {}
    for i in range(len(sets)):
        for j in range(len(sets)):
            if i != j:
                res["{" + str(sets[i]) + "} | {" + str(sets[j]) + "}"] = sets[i] | sets[j]
                res["{" + str(sets[i]) + "} & {" + str(sets[j]) + "}"] = sets[i] & sets[j]
                res["{" + str(sets[i]) + "} - {" + str(sets[j]) + "}"] = sets[i] - sets[j]
                res["{" + str(sets[j]) + "} - {" + str(sets[i]) + "}"] = sets[j] - sets[i]

    return res


if __name__ == '__main__':
    print(ex7({1, 2}, {2, 3}))