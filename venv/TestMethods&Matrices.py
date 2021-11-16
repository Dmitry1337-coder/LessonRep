from main import Matrices


matrix1 = Matrices(3, 3)
matrix1.writeMatrix()
matrix2 = Matrices(3, 4)
matrix2.writeMatrix()
print("Матрица №1:")
matrix1.showMatrix()
print("Матрица №2:")
matrix2.showMatrix()
print("\nМетод умножения функции на число:")
matrix1.mulOnConstant()
print("\nМетод сложения матриц:")
matrix2+matrix1
print("\nМетод разности матриц:")
matrix2-matrix1
print("\nМетод умножения матриц друг на друга:")
matrix2*matrix1
print("\nМетод умножения с поменянными местами матрицами:")
matrix1*matrix2
print("\nМетод возведения матрицы в степень:")
matrix1.exponentiationMatrix()
print("\nМетод транспонирования для матрицы 1:")
matrix1.transpositionMatrix()
print("\nМетод транспонирования для матрицы 2:")
matrix2.transpositionMatrix()
print("Проверка на изменение начальных матриц:")
print("Матрица №1:")
matrix1.showMatrix()
print("Матрица №2:")
matrix2.showMatrix()
print("Начальные матрицы остались неизмененными после выполнения действий с ними.")
