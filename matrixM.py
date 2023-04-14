import numpy as np
def matrixM(A,B):
    rowA = len(A)
    colA = (len(A[0]))
    rowB = len(B)
    colB = (len(B[0]))

    if colA == rowB:
        C = np.zeros((rowA, colB))
        for i in range(rowA):
            for j in range(colB):
                for k in range(colA):
                    C[i][j] = C[i][j] + (A[i][k]*B[k][j])
        return C
    else:
        return "Error"

A = [[1],[1]]
B = [[1,2]]

print(matrixM(A,B))