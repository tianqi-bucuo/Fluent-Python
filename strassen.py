def matrix_add(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    matrix_c = [[] for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix_c_temp = matrix_a[i][j] + matrix_b[i][j]
            matrix_c[i].append(matrix_c_temp)
    return matrix_c


def matrix_minus(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    matrix_c = [[] for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix_c_temp = matrix_a[i][j] - matrix_b[i][j]
            matrix_c[i].append(matrix_c_temp)
    return matrix_c


def matrix_divide(matrix_a, row, column):
    length = len(matrix_a)
    matrix_b = [[] for i in range(length // 2)]
    k = 0
    for i in range((row - 1) * length // 2, row * length // 2):
        for j in range((column - 1) * length // 2, column * length // 2):
            matrix_c_temp = matrix_a[i][j]
            matrix_b[k].append(matrix_c_temp)
        k += 1
    return matrix_b


def matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22):
    length = len(matrix_11)
    matrix_all = [[] for i in range(length * 2)]
    for i in range(length):
        matrix_all[i] = matrix_11[i] + matrix_12[i]
    for j in range(length):
        matrix_all[length + j] = matrix_21[j] + matrix_22[j]
    return matrix_all


def strassen(matrix_a, matrix_b):
    rows = len(matrix_a)
    if rows == 1:
        matrix_all = [[] for i in range(rows)]
        matrix_all[0].append(matrix_a[0][0] * matrix_b[0][0])
    else:
        s1 = matrix_minus((matrix_divide(matrix_b, 1, 2)), (matrix_divide(matrix_b, 2, 2)))
        s2 = matrix_add((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 1, 2)))
        s3 = matrix_add((matrix_divide(matrix_a, 2, 1)), (matrix_divide(matrix_a, 2, 2)))
        s4 = matrix_minus((matrix_divide(matrix_b, 2, 1)), (matrix_divide(matrix_b, 1, 1)))
        s5 = matrix_add((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 2, 2)))
        s6 = matrix_add((matrix_divide(matrix_b, 1, 1)), (matrix_divide(matrix_b, 2, 2)))
        s7 = matrix_minus((matrix_divide(matrix_a, 1, 2)), (matrix_divide(matrix_a, 2, 2)))
        s8 = matrix_add((matrix_divide(matrix_b, 2, 1)), (matrix_divide(matrix_b, 2, 2)))
        s9 = matrix_minus((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 2, 1)))
        s10 = matrix_add((matrix_divide(matrix_b, 1, 1)), (matrix_divide(matrix_b, 1, 2)))
        p1 = strassen(matrix_divide(matrix_a, 1, 1), s1)
        p2 = strassen(s2, matrix_divide(matrix_b, 2, 2))
        p3 = strassen(s3, matrix_divide(matrix_b, 1, 1))
        p4 = strassen(matrix_divide(matrix_a, 2, 2), s4)
        p5 = strassen(s5, s6)
        p6 = strassen(s7, s8)
        p7 = strassen(s9, s10)
        c11 = matrix_add(matrix_add(p5, p4), matrix_minus(p6, p2))
        c12 = matrix_add(p1, p2)
        c21 = matrix_add(p3, p4)
        c22 = matrix_minus(matrix_add(p5, p1), matrix_add(p3, p7))
        matrix_all = matrix_merge(c11, c12, c21, c22)
    return matrix_all


def main():
    a = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    b = [[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]]
    c = strassen(a, b)
    print(c)


if __name__ == '__main__':
    main()