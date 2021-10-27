from main import Matrices

matrix1 = Matrices(3, 3)
matrix1.writeMatrix()
matrix2 = Matrices(3, 3)
matrix2.writeMatrix()
print("Матрица №1:")
matrix1.ShowMatrix()
print("Матрица №2:")
matrix2.ShowMatrix()
constant = 6
print("\nМетод умножения функции на число:")
matrix1.MultiplyMatricesOnConstant(constant)
print("\nМетод сложения матриц:")
matrix2.additionMatrices(matrix1)
print("\nМетод разности матриц:")
matrix2.differenceMatrices(matrix1)
