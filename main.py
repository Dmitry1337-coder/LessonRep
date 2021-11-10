import copy
import random
from abc import ABC


class Menu(ABC):
    action = int

    @staticmethod
    def MainMenu():
        print("1. Сложение матриц")
        print("2. Вычитание матриц")
        print("3. Умножение матриц")
        print("4. Транспонирование матриц")
        print("5. Умножение матриц на число")
        print("0. Выход")

    @staticmethod
    def InputMatrix1():
        print("Введите количество строк матрицы 1:")
        cntlines = Expectation.int_expect()
        print("Введите количество столбцов матрицы 1:")
        cntcolumns = Expectation.int_expect()
        matrix1 = Matrices(cntlines, cntcolumns)
        matrix1.writeMatrix()
        return matrix1

    @staticmethod
    def InputMatrix2():
        print("Введите количество строк матрицы 2:")
        cntlines = Expectation.int_expect()
        print("Введите количество столбцов матрицы 2:")
        cntcolumns = Expectation.int_expect()
        matrix2 = Matrices(cntlines, cntcolumns)
        matrix2.writeMatrix()
        return matrix2


    @staticmethod
    def ActionMenu():
        Menu.MainMenu()
        print("Введите номер действия: ")
        action = Expectation.int_expect()
        print("Введите матрицы:")
        matrix1 = Menu.InputMatrix1()
        matrix2 = Menu.InputMatrix2()
        while action != 0:
            if action == 1:
                matrix1 + matrix2
                break
            elif action == 2:
                matrix1 - matrix2
                break
            elif action == 3:
                matrix1 * matrix2
                break
            elif action == 4:
                print("Какую матрицу вы хотите транспонировать?")
                value = Expectation.int_expect()
                if value == 1:
                    matrix1.TranspositionMatrix()
                if value == 2:
                    matrix2.TranspositionMatrix()
                else:
                    print("У вас весего лишь две матрицы. Введите 1 или 2!")
                break
            elif action == 5:
                print("Какую матрицу вы хотите умножить на число?")
                value = Expectation.int_expect()
                if value == 1:
                    matrix1.mulOnConstant()
                if value == 2:
                    matrix2.mulOnConstant()
                else:
                    print("У вас весего лишь две матрицы. Введите 1 или 2!")
                break


class Expectation(ABC):

    @staticmethod
    def int_expect():
        expectation = True
        value = 0
        while expectation:
            try:
                expectation = False
                value = int(input())
            except ValueError:
                print("Требуется целочисленное значение!")
                expectation = True
        return value


class Matrices:
    def __init__(self, cntlines, cntcolumns):
        self.cntlines = cntlines
        self.cntcolumns = cntcolumns
        self.matrix = [[0 for j in range(cntcolumns)] for i in range(cntlines)]

    def ShowMatrix(self):
        for i in self.matrix:
            print(i)

    def writeMatrix(self):
        print(f"\nВведите матрицу(по элементно):")
        list = self.matrix.copy()
        for i in range(self.cntlines):
            print(f"Введите {i + 1} строку:")
            for j in range(self.cntcolumns):
                list[i][j] = Expectation.int_expect()
        self.matrix = list

    def __add__(self, other):
        if (self.cntlines == other.cntlines) and \
                (self.cntcolumns == other.cntcolumns) and \
                (isinstance(other, Matrices)):
            list = [[0 for i in range(self.cntcolumns)] for j in range(self.cntlines)]
            for i in range(self.cntlines):
                for j in range(self.cntcolumns):
                    list[i][j] = self.matrix[i][j] + other.matrix[i][j]
                print(list[i])
            return list
        else:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    def __sub__(self, other):
        if (self.cntlines == other.cntlines) and \
                (self.cntcolumns == other.cntcolumns) and \
                (isinstance(other, Matrices)):
            list = [[0 for i in range(self.cntcolumns)] for j in range(self.cntlines)]
            for i in range(self.cntlines):
                for j in range(self.cntcolumns):
                    list[i][j] = self.matrix[i][j] - other.matrix[i][j]
                print(list[i])
            return list
        else:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    def mulOnConstant(self):
        number = Expectation.int_expect()
        list = [[0 for i in range(self.cntcolumns)] for j in range(self.cntlines)]
        for i in range(self.cntlines):
            for j in range(self.cntcolumns):
                list[i][j] = self.matrix[i][j] * number
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
            print('Матрицы нельзя умножить,т.к. кол-во эл. в столбце 1-ой матрицы, не соотв. кол-ву строк эл. во 2-ой')

    def TranspositionMatrix(self):
        list = [[0 for j in range(self.cntlines)] for i in range(self.cntcolumns)]
        for i in range(self.cntcolumns):
            for j in range(self.cntlines):
                list[i][j] = self.matrix[j][i]
            print(list[i])

    def ExponentiationMatrix(self):
        num = Expectation.int_expect()
        if self.cntlines == self.cntcolumns:
            object = copy.copy(self)
            for i in range(num - 1):
                print(f"{i + 1}-й шаг:")
                object.matrix = self*object
            print("Результат возведения в степень")
            object.ShowMatrix()
        else:
            print("Чтобы возвести матрицу в степень, она должна быть квадратной!")

    def WriteMatrixToFile(self):
        file = open(f"{random.randint(0, 10000)} matrix.txt", 'a')
        for i in range(self.cntlines):
            for j in range(self.cntcolumns):
                file.write(str(self.matrix[i][j]) + ' ')
            file.write('\n')
        file.close()

    def WritingFromFile(self):
        file = open(f"123 matrices.txt", "r+")
        arr_1 = []
        arr = file.readlines()
        for str in arr:
            arr_1.append(str.split('.'))
        for str in arr_1:
            if str[0] == "matrix":
                print("Матрица № -", str[1])
            print(str)
        print("Введите номер матрицы, которую хотите использовать:")
        number = Expectation.int_expect()
        print(number)
        counter = 0
        cnt = 0
        print(arr, '\n')
        print(arr_1)
        for str in arr_1:
            flag = False
            if number == str[1] and str[0] == 'matrix':
                print("матрица успешно выбрана")
                self.cntlines = int(str[2])
                self.cntcolumns = int(str[3])
                flag = True
                counter = self.cntlines
                cnt = copy.copy(counter)
            list = [[0 for i in range(self.cntcolumns)] for j in range(self.cntlines)]
            if flag and counter > 0:
                counter -= 1
                for j in range(self.cntlines):
                    list[cnt-counter][j] = int(str[j])
        self.ShowMatrix()




# наш скрипт

if __name__ == '__main__':
    Menu.ActionMenu()

