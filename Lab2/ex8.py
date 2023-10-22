def ex8(strings, x=1, flag=True):
    res = []
    for string in strings:
        chars = []
        for char in string:
            if flag:
                if ord(char) % x == 0:
                    chars.append(char)
            else:
                if ord(char) % x != 0:
                    chars.append(char)
        res.append(chars)

    return res


if __name__ == '__main__':
    print(ex8(x=2, strings=["test", "hello", "lab001"], flag=False))