def ex1(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fibo = [0, 1]
    while len(fibo) < n:
        fibo.append(fibo[len(fibo) - 1] + fibo[len(fibo) - 2])

    return fibo


if __name__ == '__main__':
    print(ex1(15))