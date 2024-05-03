import numpy as np


def cholesky(A):
    n = len(A)
    L = np.zeros_like(A, dtype=float)
    L[0][0] = np.sqrt(A[0][0])
    for i in range(1, n):
        for j in range(i + 1):
            if i == j:
                sum_for_ii = 0.0
                for p in range(i):
                    sum_for_ii += L[i][p] ** 2
                L[i][i] = np.sqrt(A[i][i] - sum_for_ii)
            else:
                sum_for_ij = 0.0
                for p in range(i):
                    sum_for_ij += L[i][p] * L[j][p]
                L[i][j] = (A[i][j] - sum_for_ij) / L[j][j]

    return L


if __name__ == "__main__":
    L = np.array(
        [
            [1.0, 0.0, 0.0],
            [4.0, 2.0, 0.0],
            [6.0, 5.0, 3.0],
        ]
    )

    A = L @ L.T
    L = cholesky(A)
    print(L)
