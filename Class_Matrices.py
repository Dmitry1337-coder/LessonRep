import copy
import random

from Class_Exception import ExceptionClass


class Matrices:
    def __init__(self, count_lines, count_columns):
        self.count_lines = count_lines
        self.count_columns = count_columns
        self.matrix = self.__null_Matrix(self.count_lines, self.count_columns)

    def showMatrix(self):
        for i in self.matrix:
            print(i)

    def writeMatrix(self):
        print("Введите матрицу:")
        for i in range(self.count_lines):
            self.matrix[i] = ExceptionClass.list_expect(self.count_columns)

    def __add__(self, other):
        if (self.count_lines == other.count_lines) and \
                (self.count_columns == other.count_columns) and \
                (isinstance(other, Matrices)):
            list_matrix = self.__null_Matrix(self.count_lines, self.count_columns)
            for i in range(self.count_lines):
                for j in range(self.count_columns):
                    list_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                #print(list_matrix[i])
            return list_matrix #list_matrix[i]
        else:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    def __sub__(self, other):
        if (self.count_lines == other.count_lines) and \
                (self.count_columns == other.count_columns) and \
                (isinstance(other, Matrices)):
            list_matrix = self.__null_Matrix(self.count_lines, self.count_columns)
            for i in range(self.count_lines):
                for j in range(self.count_columns):
                    list_matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
                #print(list_matrix[i])
            return list_matrix #list_matrix
        else:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    def mulOnConstant(self, number):
        list_matrix = self.__null_Matrix(self.count_lines, self.count_columns)
        for i in range(self.count_lines):
            for j in range(self.count_columns):
                list_matrix[i][j] = self.matrix[i][j] * number
            #print(list_matrix[i])

    def __mul__(self, other):
        list_matrix = self.__null_Matrix(self.count_lines, other.count_columns)
        if not isinstance(other, Matrices) or self.count_columns != other.count_lines:
            print('Матрицы нельзя умножить,т.к. кол-во эл. в столбце 1-ой матрицы, не соотв. кол-ву строк эл. во 2-ой')
        else:
            for i in range(self.count_lines):
                for j in range(other.count_columns):
                    for k in range(self.count_columns):
                        list_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return list_matrix

    def transpositionMatrix(self):
        list_matrix = self.__null_Matrix(self.count_columns, self.count_lines)
        for i in range(self.count_columns):
            for j in range(self.count_lines):
                list_matrix[i][j] = self.matrix[j][i]
            #print(list_matrix[i])
        return list_matrix

    def exponentiationMatrix(self, number):
        if self.count_lines == self.count_columns:
            other = copy.copy(self)
            for i in range(number - 1):
                other.matrix = self*other
            return other.matrix
        else:
            print("Чтобы возвести матрицу в степень, она должна быть квадратной!")

    def writeMatrixToFile(self):
        file_name = open(f"{random.randint(0, 10000)} matrix.txt", 'a')
        for i in range(self.count_lines):
            for j in range(self.count_columns):
                file_name.write(str(self.matrix[i][j]) + ' ')
            file_name.write('\n')
        file_name.close()

    @staticmethod
    def __null_Matrix(cnt_lines, cnt_columns):
        null_matrix_list = [[0 for _ in range(cnt_columns)] for _ in range(cnt_lines)]
        return null_matrix_list
