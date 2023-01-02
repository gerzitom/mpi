from config import *
import ComputationResult

# jacobi's method

# https://stackoverflow.com/questions/43074634/checking-if-a-matrix-is-diagonally-dominant-in-python
# check whether convergence criteria is met (matrix must be diagonally dominant)


def jacobi(matrix, vector, matrixD):
    if not isDiagonallyDominant(matrix):
        raise Exception("Matrix is not diagonally dominant.")

    iterationCount = 0
    iterationVector = np.zeros(20)

    matrixDInversion = la.inv(matrixD)

    matrixDifference = matrixD - matrix

    residue = matrix @ iterationVector - vector

    rightSideNorm = la.norm(vector)
    residueNorm = la.norm(residue)

    result = residueNorm / rightSideNorm

    while result > precision:
        iterationCount += 1
        # x_k = D^-1 * [(D - A) * x_k-1 + b]
        iterationVector = matrixDInversion @ (matrixDifference @ iterationVector + vector)
        residue = matrix @ iterationVector - vector
        residueNorm = la.norm(residue)
        result = residueNorm / rightSideNorm

    return ComputationResult.ComputationResult(iterationCount, iterationVector)


def isDiagonallyDominant(givenMatrix):
    abs_x = np.abs(givenMatrix)
    return np.all(2 * np.diag(abs_x) >= np.sum(abs_x, axis=1))