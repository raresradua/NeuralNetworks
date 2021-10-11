from in_python import *
from with_numpy import solve_equation
import numpy


if __name__ == '__main__':
    print("""
        IN PURE PYTHON
    """)
    A, B = parse_eq("eq.txt")
    print("A: ", A)
    print("B: ", B)

    det_A = determinant(A)
    print("Determinant A: ", det_A)
    transpose_A = transpose(A)
    print("A Transpose: ", transpose_A)
    adjoint_A = adjoint_matrix(transpose_A)
    print("A Adjoint: ", adjoint_A)
    inverse_A = inverse(adjoint_A, det_A)
    print("A Inverse: ", inverse_A)
    X = matrix_product(inverse_A, B)
    print(X)

    print("""
        WITH NUMPY
    """)
    A, B = parse_eq("eq.txt")
    X = solve_equation(A, B)
    print(X)
