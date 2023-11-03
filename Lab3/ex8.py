def ex8(mapping):
    key = 'start'
    visited = set()
    result = []

    while key not in visited and key in mapping and mapping[key] != key:
        visited.add(key)
        result.append(mapping[key])
        key = mapping[key]

    return result


if __name__ == '__main__':
    print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
