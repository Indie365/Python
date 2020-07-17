from decimal import *


def inverse_of_matrix(matrix):
    """
    A matrix multiplied with its inverse gives the identity matrix.
    This function finds the inverse of a 2x2 matrix.
    If the determinant of a matrix is 0, its inverse does not exist.

    Sources for fixing inaccurate float arithmetic:
    https://stackoverflow.com/questions/6563058/how-do-i-use-accurate-float-arithmetic-in-python
    https://docs.python.org/release/2.7/library/decimal.html#module-decimal

    >>> inverse_of_matrix([[2, 5], [2, 0]])
    [[0.0, 0.5], [0.2, -0.2]]
    >>> inverse_of_matrix([[2.5, 5], [1, 2]])
    'Does not exist'
    >>> inverse_of_matrix([[12, -16], [-9, 0]])
    [[0.0, -0.1111111111111111], [-0.0625, -0.08333333333333333]]
    >>> inverse_of_matrix([[12, 3], [16, 8]])
    [[0.16666666666666666, -0.0625], [-0.3333333333333333, 0.25]]
    >>> inverse_of_matrix([[10, 9], [2, 2.5]])
    [[1.0, -4.5], [-1.0, 5.0]]
    """

    determinant = Decimal(matrix[0][0]) * Decimal(matrix[1][1]) - Decimal(
        matrix[1][0]
    ) * Decimal(
        matrix[0][1]
    )  # Finds the determinant of the matrix
    if determinant != 0:
        inverse = []
        matrix_with_swapped_pos = (
            [] + matrix
        )  # Creates a copy of the matrix and swaps the positions of the elements
        matrix_with_swapped_pos[0][0], matrix_with_swapped_pos[1][1] = (
            matrix[1][1],
            matrix[0][0],
        )
        matrix_with_swapped_pos[1][0], matrix_with_swapped_pos[0][1] = (
            0 - matrix[1][0],
            0 - matrix[0][1],
        )
        for row1 in matrix_with_swapped_pos:
            inverse.append(
                [float(Decimal(num) / determinant) for num in row1]
            )  # Finds the inverse of the matrix
        for row2 in inverse:
            for index in range(len(row2)):  # Replaces the -0.0's with 0.0's
                if row2[index] == -0.0:
                    row2[index] = 0.0
        return inverse
    else:
        return "Does not exist"
