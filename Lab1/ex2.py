def ex2(string):
    chars = [*string]
    vowels_count = 0
    for char in chars:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowels_count += 1

    return vowels_count


if __name__ == '__main__':
    inputStr = input()
    print(ex2(inputStr))
