#!/usr/bin/env python3

cov_matrix = [ [ 0 for i in range(3) ] for j in range(3) ]

matrix = [
    [10, 6, 17],
    [4, 9, 1],
    [12, 6, 11],
    [13, 5, 19],
    [6, 9, 2]
]

def print_matrix():
    for i in range(3):
        for j in range(3):
            print(cov_matrix[i][j], end=" ")
        print()

def cov():
    for i in range(3):
            for j in range(3):
                a = b = c = 0
                for k in range(5):
                    a += (matrix[k][i] * matrix[k][j])
                    b += matrix[k][i]
                    c += matrix[k][j]

                cov_matrix[i][j] = (1/5 * a - 1/25 * b * c)

cov()

print_matrix()
