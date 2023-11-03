def ex3(val1, val2):
    if type(val1) is not type(val2):
        return False

    if isinstance(val1, dict):
        if len(val1) != len(val2):
            return False
        for key in val1:
            if key not in val2:
                return False
            if not ex3(val1[key], val2[key]):
                return False

    elif isinstance(val1, (list, tuple)):
        if len(val1) != len(val2):
            return False
        for item1, item2 in zip(val1, val2):
            if not ex3(item1, item2):
                return False

    else:
        if val1 != val2:
            return False

    return True


if __name__ == '__main__':
    print(ex3(
        {'a': 1, 'b': [1, 2], 12: [1, (2, 3)]},
        {'a': 1, 'b': [1, 2], 12: [1, (2, 3)]},
        # {'a': 1, 'b': [1, 2], 12: [1, (3, 4)]},
    ))
