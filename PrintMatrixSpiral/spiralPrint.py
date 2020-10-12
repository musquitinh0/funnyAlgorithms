"""
This program print the matrix in spiral form.
This problem has been solved through recursive way.
      Matrix must satisfy below conditions
        i) matrix should be only one or two dimensional
        ii)column of all the row should be equal
"""


def spiralPrint(matrix):
    ls=list()
    while matrix:
        ls.extend(matrix[0])
        #print(ls)
        matrix=list(zip(*matrix[1:]))[::-1]
        #print(matrix)
    print(ls)


# driver code
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
spiralPrint(a)