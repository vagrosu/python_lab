def ex2(text):
    occurences = {}
    for char in text:
        if char not in occurences:
            occurences[char] = 1
        else:
            occurences[char] += 1

    return occurences


if __name__ == '__main__':
    print(ex2("Ana has apples."))
