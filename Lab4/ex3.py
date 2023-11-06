class Matrix:
    def __init__(self, n, m, init=None):
        self.rows = n
        self.cols = m
        if init:
            self.data = init
        else:
            self.data = [[0 for _ in range(m)] for _ in range(n)]

    def get_element(self, row, col):
        return self.data[row][col]

    def set_element(self, row, col, value):
        self.data[row][col] = value

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for row in range(self.rows):
            for col in range(self.cols):
                result.set_element(col, row, self.get_element(row, col))

        return result

    def multiply(self, matrix):
        if self.cols != matrix.rows:
            return None

        result = Matrix(self.rows, matrix.cols)
        for row in range(self.rows):
            for col in range(matrix.cols):
                for i in range(self.cols):
                    result.data[row][col] += self.data[row][i] * matrix.data[i][col]

        return result

    def apply_func(self, func):
        for row in range(self.rows):
            for col in range(matrix.cols):
                self.data[row][col] = func(self.data[row][col])


if __name__ == '__main__':
    matrix = Matrix(2, 3)
    matrix.set_element(0, 0, 1)
    matrix.set_element(0, 1, 2)
    matrix.set_element(0, 2, 3)
    matrix.set_element(1, 0, 4)
    matrix.set_element(1, 1, 5)
    matrix.set_element(1, 2, 6)

    matrix2 = Matrix(4, 2, [[1, 2], [3, 4], [5, 6], [7, 8]])
    print("Matrix2:")
    for row in range(matrix2.rows):
        for col in range(matrix2.cols):
            print(matrix2.get_element(row, col), end=' ')
        print()

    print("Matrix:")
    for row in range(matrix.rows):
        for col in range(matrix.cols):
            print(matrix.get_element(row, col), end=' ')
        print()

    print("Transposed matrix:")
    transposed = matrix.transpose()
    for row in range(transposed.rows):
        for col in range(transposed.cols):
            print(transposed.get_element(row, col), end=' ')
        print()

    print("Multiplied matrix:")
    multiplied = matrix.multiply(transposed)
    if multiplied:
        for row in range(multiplied.rows):
            for col in range(multiplied.cols):
                print(multiplied.get_element(row, col), end=' ')
            print()
    else:
        print("Cannot multiply matrices")

    print("Squared elements matrix:")
    matrix.apply_func(lambda x: x ** 2)
    for row in range(matrix.rows):
        for col in range(matrix.cols):
            print(matrix.get_element(row, col), end=' ')
        print()