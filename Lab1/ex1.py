from math import gcd


def ex1():
    input_string = input()
    numbers = input_string.split(' ')

    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])

    answer = gcd(numbers[0], numbers[1])
    for i in range(2, len(numbers)):
        answer = gcd(answer, numbers[i])

    print(answer)


if __name__ == '__main__':
    ex1()
