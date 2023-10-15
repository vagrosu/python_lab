def ex6(num):
    num_copy = num
    rev_num = 0
    while num_copy:
        rev_num = rev_num * 10 + num_copy % 10
        num_copy //= 10

    return num == rev_num


if __name__ == '__main__':
    input_number = int(input("Enter a number: "))
    print(ex6(input_number))