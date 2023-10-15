def ex5(matrix):
    res = ""

    rows, cols = len(matrix), len(matrix[0])
    top_row, bottom_row, left_col, right_col = 0, rows - 1, 0, cols - 1
    while top_row <= bottom_row and left_col <= right_col:
        for j in range(left_col, right_col + 1):
            res += matrix[top_row][j]
        top_row += 1

        for i in range(top_row, bottom_row + 1):
            res += matrix[i][right_col]
        right_col -= 1

        if top_row <= bottom_row:
            for j in range(right_col, left_col - 1, -1):
                res += matrix[bottom_row][j]
            bottom_row -= 1

        if left_col <= right_col:
            for i in range(bottom_row, top_row - 1, -1):
                res += matrix[i][left_col]
            left_col += 1

    return res

if __name__ == '__main__':
    matrix = [['f', 'i', 'r', 's'],
            ['n', '_', 'l', 't'],
            ['o', 'b', 'a', '_'],
            ['h', 't', 'y', 'p']]
    print(ex5(matrix))