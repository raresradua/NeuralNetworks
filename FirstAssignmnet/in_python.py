def parse_eq(file_name):
    """
    Parses file and constructs matrices A, B that contains the coefficients of the equation system and the result of them
    respectively

    :param file_name: name of the file
    :return: matrix A that contains coefficients of the equations, matrix B contains the results of the equations
    """
    A = list()
    B = list()
    f = open(file_name)
    for line in f:
        sign = 1
        coef = 0
        x_coef = 0
        y_coef = 0
        z_coef = 0

        line = (line.replace(" ", "")).split("=")   # remove spaces and split the equation and result
        B.append([int(line[1].strip())])    # append 'row' to B

        for chr in line[0]:
            sign = 1 if chr == "+" else (0 if chr == "-" else sign)  # coefficient sign

            coef = coef * 10 + int(chr) if chr in "0123456789" else coef    # if chr is in '0123456789' else do nothing
            coef = 1 if coef == 0 and chr in "xyz" else coef    # if chr in 'xyz' and coef == 0 else do nothing

            if chr == "x":
                x_coef = coef if sign else coef * -1
                coef = 0
            if chr == "y":
                y_coef = coef if sign else coef * -1
                coef = 0
            if chr == "z":
                z_coef = coef if sign else coef * -1
                coef = 0

        A.append([x_coef, y_coef, z_coef])

    f.close()
    return A, B


def determinant(A):
    """
    Calculates the determinant of a matrix A
    :param A: matrix A
    :return: determinant of the matrix A
    """
    det = 0
    if len(A) == 2 and len(A[0]) == 2:
        return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

    for i in range(0, len(A)):
        A_submatrix = A[1:] # remove 1st row
        for j in range(0, len(A_submatrix)):
            A_submatrix[j] = A_submatrix[j][0:i] + A_submatrix[j][(i+1):] # remove the column
        sign = (-1) ** (i % 2)
        submatrix_det = determinant(A_submatrix)
        det += sign * A[0][i] * submatrix_det
    return det if det != 0 else False


def transpose(A):
    """
    Calculates the transpose matrix of A. Rows become columns, columns become rows
    :param A: matrix A
    :return: transpose matrix of A
    """
    A_T = list()
    nr_cols = len(A[0])
    nr_rows = len(A)
    for i in range(0, nr_cols):
        transpose_row = list()
        for j in range(0, nr_rows):
            transpose_row.append(A[j][i])
        A_T.append(transpose_row)
    return A_T


def adjoint_matrix(A_T):
    """
    Calculates the adjoint matrix of A using its transpose matrix.

    :param A_T: transpose matrix of A
    :return: adjoint matrix of A
    """
    nr_cols = len(A_T[0])
    nr_rows = len(A_T)
    A_adjoint = list()
    for i in range(0, nr_cols):
        adjoint_col = list()
        for j in range(0, nr_rows):
            submatrix = A_T[0:j] + A_T[j + 1:]  # remove the row
            for j_s in range(0, len(submatrix)):
                submatrix[j_s] = submatrix[j_s][0:i] + submatrix[j_s][(i + 1):]
            det = determinant(submatrix)
            adjoint_col.append(((-1) ** (i + j)) * det)
        A_adjoint.append(adjoint_col)
    return transpose(A_adjoint)


def inverse(adjoint_A, det_A):
    """
    Calculates the inverse of matrix A using the adjoint matrix and the determinant of matrix A
    :param adjoint_A: adjoint matrix of A
    :param det_A: determinant of A
    :return:
    """
    if det_A == False:
        exit("Determinant is 0")
    inverse_A = list()
    for row in adjoint_A:
        new_row = list()
        for el in row:
            new_row.append(el * (det_A ** (-1)))
        inverse_A.append(new_row)
    return inverse_A


def matrix_product(M1, M2):
    """
    Multiplies 2 matrices and for our problem we use it to get the solutions of the equations
    :param M1: first matrix
    :param M2: second matrix
    :return: product of M1 and M2
    """
    X = list()
    for i in range(0, len(M1)):
        row = list()
        for j in range(0, len(M2[0])):
            row.append(0)
        X.append(row)

    for i in range(0, len(M1)):
        for j in range(0, len(M2[0])):
            for k in range(len(M2)):
                X[i][j] += M1[i][k] * M2[k][j]
            X[i][j] = round(X[i][j])
    return X

