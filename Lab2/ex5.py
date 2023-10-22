def ex5(matrix):
    mat_copy = matrix
    for i in range(0, len(mat_copy)):
        for j in range(0, len(mat_copy[i])):
            if i > j:
                mat_copy[i][j] = 0

    return mat_copy


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(ex5(matrix))