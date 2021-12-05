# блок импорта

# блок глобальных переменных

# блок функций
#def menu():
#    print(f"""1. Add matrices
#2. Multiply matrix to a constant
#3. Multiply matrices
#4. Transpose matrix
#5. Calculate a determinant
#6. Inverse matrix
#0. Exit""")
#def additionMatrices(self, secondMatrix):
#    if ((firstMatrix.cntlines == secondMatrix.cntlines) and ((firstMatrix.cntcolumns == secondMatrix.cntcolumns))):
#        additionlist = [[i for j in range(firstMatrix.cntcolumns)] for i in range(firstMatrix.cntlines)]
#        for i in range(len(firstMatrix.matrix)):
#           for j in range(len(firstMatrix.matrix[i])):
#                additionlist[i][j] = secondMatrix.matrix[i][j] + firstMatrix.matrix[i][j]
#            print(additionlist[i])

#def differenceMatrices(firstMatrix, secondMatrix):
#    if ((firstMatrix.cntlines == secondMatrix.cntlines) and ((firstMatrix.cntcolumns == secondMatrix.cntcolumns))):
#        additionlist = [[i for j in range(firstMatrix.cntcolumns)] for i in range(firstMatrix.cntlines)]
#        for i in range(len(firstMatrix.matrix)):
#            for j in range(len(firstMatrix.matrix[i])):
#                additionlist[i][j] = secondMatrix.matrix[i][j] - firstMatrix.matrix[i][j]
#            print(additionlist[i])


# блок классов
import copy
import random

    @staticmethod
    def actionSubtraction():
        print("Введите матрицы, которые вы хотите вычесть друг из друга:")
        matrix1 = Menu.InputMatrix()
        matrix2 = Menu.InputMatrix()
        matrix1 - matrix2

class Matrices:
    counter = 1
    def __init__(self, cntlines, cntcolumns):
        self.cntlines = cntlines
        self.cntcolumns = cntcolumns
        self.matrixID = copy.deepcopy(self.counter)
        self.matrix = [[0 for j in range(cntcolumns)] for i in range(cntlines)]
        self.counter +=1

    def ShowMatrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def writeMatrix(self):
        print(f"\nВведите матрицу:")
        list = self.matrix.copy()
        for i in range(len(list)):
            print(f"Введите {i+1} строку:")
            for j in range(len(list[i])):
                try:
                    expectation = False
                    list[i][j] = int(input())
                except ValueError:
                    print("ValueError(Требуется целочисленное значение. Введите матрицу заново)")
                    expectation = True
                    self.writeMatrix()
                    break
            if expectation:
                break
        self.matrix = list

    def __add__(self, other):
        if (self.cntlines == other.cntlines) and \
                (self.cntcolumns == other.cntcolumns):
            list = self.matrix.copy()
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    list[i][j] = self.matrix[i][j] + other.matrix[i][j]
                print(list[i])
        else:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    def __sub__(self, other):
        if (self.cntlines == other.cntlines) and \
                (self.cntcolumns == other.cntcolumns) and \
                (isinstance(other, Matrices)):
            additionlist = self.matrix.copy()
            for i in range(self.cntlines):
                for j in range(self.cntcolumns):
                    additionlist[i][j] = self.matrix[i][j] - other.matrix[i][j]
                print(additionlist[i])
            return additionlist
        else:
            print("Вычитание матриц невозмиожно осуществить, так как кол-во строк и столбцов в них разное!")


    def __mul__(self, number):
        list = self.matrix.copy()
        for i in range(self.cntlines):
            for j in range(self.cntcolumns):
                list[i][j] *= number
            print(list[i])

    def __mul__(self, other):
        list = [[0 for i in range(other.cntcolumns)] for j in range(self.cntlines)]
        if (isinstance(other, Matrices) and (self.cntcolumns == other.cntlines)):
            for i in range(self.cntlines):
                for j in range(other.cntcolumns):
                    for k in range(self.cntcolumns):
                        list[i][j] += self.matrix[i][k] * other.matrix[k][j]
                print(list[i])
            return list
        else:
            print('Матрицы нельзя умножить,т.к. кол-во эл. в столбце 1-ой матрицы, не соотв. кол-ву эл. во 2-ой')


    def TransponMatrix(self):
        list = [[0 for j in range(self.cntlines)] for i in range(self.cntcolumns)]
        for i in range(self.cntcolumns):
            for j in range(self.cntlines):
                list[i][j] = self.matrix[j][i]
            print(list[i])

    def ExponentiationOfTheMatrix(self, degree):
        if (self.cntlines == self.cntcolumns):
            object = copy.copy(self)
            for i in range(degree-1):
                object.matrix = self.__mul__(object)

    def WriteMatrixToFile(self):
        file = open(f"{random.randint(0, 10000)} matrix.txt", 'a')
        file.write(str(self.cntlines)+' '+str(self.cntcolumns)+'\n')
        for i in range(self.cntlines):
            for j in range(self.cntcolumns):
                file.write(str(self.matrix[i][j])+' ')
            file.write('\n')
        file.close()



# наш скрипт

if __name__ == '__main__':
    #menu()
    #print(f"Your choice:")
    #choice = input()
    #print()
    matrix1 = Matrices(3,3)
    matrix2 = Matrices(3,3)
    matrix1.writeMatrix()
    matrix2.writeMatrix()
    matrix2.ShowMatrix()
    print()
    matrix1.ShowMatrix()
    print()
   # matrix2.MultiplyMatricesByEachOther(matrix1)
    #matrix1.TransponMatrix()
    #matrix1.ExponentiationOfTheMatrix(5)
    #print()
    #matrix1.ShowMatrix()
    matrix2 - matrix1
    print()
    print()
    print()
    matrix2.WriteMatrixToFile()