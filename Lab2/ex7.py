def ex7(numbers):
    greatest_palindrome = 0
    no_palindromes = 0
    for num in numbers:
        if str(num) == str(num)[::-1]:
            no_palindromes += 1
            if num > greatest_palindrome:
                greatest_palindrome = num

    return greatest_palindrome, no_palindromes


if __name__ == '__main__':
    print(ex7([12321, 123, 121, 1331, 123321, 123456, 123454321, 1234567, 123456787654321, 92345678987654329]))
