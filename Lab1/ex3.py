def ex3(str1, str2):
    return str1.count(str2)


if __name__ == '__main__':
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    print(ex3(str1, str2))