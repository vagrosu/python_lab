def ex4(str):
    char_list = [*str]
    new_str = ""
    for i in range(0, len(char_list)):
        if char_list[i].isupper():
            if i != 0:
                new_str += '_'
            new_str += char_list[i].lower()
        else:
            new_str += char_list[i]

    return new_str


if __name__ == '__main__':
    str = input("Enter string: ")
    print(ex4(str))