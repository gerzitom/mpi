from jacobi import jacobi
from gauss_seidel import gaussSeidel
from config import buildMatrix, buildRightSideVector, buildMatrixD, matrixL

def printResults(gamma):
    rightSideVector = buildRightSideVector(gamma)
    matrixD = buildMatrixD(gamma)
    givenMatrix = buildMatrix(gamma)
    print("\nGAMMA: " + str(gamma))
    print("--------------------------------------------------------------------------------------")
    print("Jacobi method: ")

    try:
        jacobiResult = jacobi(givenMatrix, rightSideVector, matrixD)
        print(jacobiResult)
    except Exception as e:
        print(e)


    print("--------------------------------------------------------------------------------------")
    print("Gauss Seidel method: ")

    try:
        gaussSeidelResult = gaussSeidel(givenMatrix, rightSideVector, matrixD, matrixL)
        print(gaussSeidelResult)
    except Exception as e:
        print(e)

    print("--------------------------------------------------------------------------------------\n")

if __name__ == "__main__":
    printResults(10)
    printResults(2)
    printResults(4/5)