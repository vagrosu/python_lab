def ex8(num):
    bin_num = int(bin(num)[2:])
    count = 0
    while bin_num:
        count += bin_num % 10
        bin_num //= 10

    return count

if __name__ == '__main__':
    input_nr = int(input())
    print(ex8(input_nr))