import ComputationResult
from config import *

# gauss-seidel method

# https://stackoverflow.com/questions/16266720/find-out-if-matrix-is-positive-definite-with-numpy
# check whether convergence criteria is met (matrix must be positive definite)

def gaussSeidel(givenMatrix, rightSide, matrixD, matrixL):
    if not isPositiveDefinite(givenMatrix):
        raise Exception("Matrix is not positive definite.")

    iterationCount = 0
    iterationVector = np.zeros(20)

    # D + L
    matrixQ = matrixD + matrixL
    matrixQInversion = la.inv(matrixQ)

    # D + L - A
    matrixDifference = matrixQ - givenMatrix

    residue = givenMatrix @ iterationVector - rightSide

    rightSideNorm = la.norm(rightSide)
    residueNorm = la.norm(residue)

    result = residueNorm / rightSideNorm

    while result > precision:
        iterationCount += 1
        # x_k = Q^-1 * [(D + L - A) * x_k-1 + b]
        iterationVector = matrixQInversion @ ((matrixDifference @ iterationVector) + rightSide)
        residue = givenMatrix @ iterationVector - rightSide
        residueNorm = la.norm(residue)
        result = residueNorm / rightSideNorm

    return ComputationResult.ComputationResult(iterationCount, iterationVector)


def isPositiveDefinite(givenMatrix):
    return np.all(np.linalg.eigvals(givenMatrix) > 0)