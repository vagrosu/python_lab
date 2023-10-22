def ex2(numbers):
    prime_numbers = []
    for num in numbers:
        if num > 1:
            for i in range(2, num // 2):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)

    return prime_numbers


if __name__ == '__main__':
    my_list = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 17, 51, 100, 200, 201, 203, 997]
    print(ex2(my_list))