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
    def InputMatrix():
        print("Введите количество строк матрицы:")
        count_lines = Expectation.int_expect()
        print("Введите количество столбцов матрицы:")
        count_columns = Expectation.int_expect()
        matrix = Matrices(count_lines, count_columns)
        matrix.writeMatrix()
        return matrix

    @staticmethod
    def ActionMenu():
        while True:
            Menu.MainMenu()
            print("Введите номер действия: ")
            action = Expectation.int_expect()
            if action == 1:
                Menu.actionAddition()
            elif action == 2:
                Menu.actionSubtraction()
            elif action == 3:
                Menu.actionMultiplication()
            elif action == 4:
                Menu.actionTranspose()
            elif action == 5:
                Menu.actionMulConstant()
            elif action == 0:
                break
            else:
                print("Нет такого действия!")
            print("Хотите вернуться в главное меню?(y/n)")
            flag = Expectation.str_expect()
            if flag == 'y':
                continue
            elif flag == 'n':
                break
            else:
                print("Вы не ввели символы 'y' или 'n', поэтому вы были переведеы в главное меню.")
                continue

    @staticmethod
    def actionAddition():
        print("Введите матрицы, которые вы хотите сложить:")
        matrix1 = Menu.InputMatrix()
        matrix2 = Menu.InputMatrix()
        matrix1 + matrix2

    @staticmethod
    def actionSubtraction():
        print("Введите матрицы, которые вы хотите вычесть друг из друга:")
        matrix1 = Menu.InputMatrix()
        matrix2 = Menu.InputMatrix()
        matrix1 - matrix2

    @staticmethod
    def actionMultiplication():
        matrix1 = Menu.InputMatrix()
        matrix2 = Menu.InputMatrix()
        matrix1 * matrix2

    @staticmethod
    def actionTranspose():
        matrix = Menu.InputMatrix()
        matrix.transpositionMatrix()

    @staticmethod
    def actionMulConstant():
        matrix = Menu.InputMatrix()
        matrix.mulOnConstant()


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

    @staticmethod
    def str_expect():
        expectation = True
        value = 0
        while expectation:
            try:
                expectation = False
                value = str(input())
            except ValueError:
                print("Требуется символьное значение!")
                expectation = True
        return value


class Matrices:
    def __init__(self, count_lines, count_columns):
        self.count_lines = count_lines
        self.count_columns = count_columns
        self.matrix = [[0 * i * j for j in range(count_columns)] for i in range(count_lines)]

    def showMatrix(self):
        for i in self.matrix:
            print(i)

    def writeMatrix(self):
        print(f"\nВведите матрицу(по элементно):")
        list_matrix = self.matrix.copy()
        for i in range(self.count_lines):
            print(f"Введите {i + 1} строку:")
            for j in range(self.count_columns):
                list_matrix[i][j] = Expectation.int_expect()
        self.matrix = list_matrix

    def __add__(self, other):
        if (self.count_lines == other.count_lines) and \
                (self.count_columns == other.count_columns) and \
                (isinstance(other, Matrices)):
            list_matrix = [[0 * i * j for i in range(self.count_columns)] for j in range(self.count_lines)]
            for i in range(self.count_lines):
                for j in range(self.count_columns):
                    list_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                print(list_matrix[i])
            return list_matrix
        else:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    def __sub__(self, other):
        if (self.count_lines == other.count_lines) and \
                (self.count_columns == other.count_columns) and \
                (isinstance(other, Matrices)):
            list_matrix = [[0 * i * j for i in range(self.count_columns)] for j in range(self.count_lines)]
            for i in range(self.count_lines):
                for j in range(self.count_columns):
                    list_matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
                print(list_matrix[i])
            return list_matrix
        else:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    def mulOnConstant(self):
        print("Введите число, на которое хотите умножить матрицу:")
        number = Expectation.int_expect()
        list_matrix = [[0 * i * j for i in range(self.count_columns)] for j in range(self.count_lines)]
        for i in range(self.count_lines):
            for j in range(self.count_columns):
                list_matrix[i][j] = self.matrix[i][j] * number
            print(list_matrix[i])

    def __mul__(self, other):
        list_matrix = [[0 * i * j for i in range(other.count_columns)] for j in range(self.count_lines)]
        if not isinstance(other, Matrices) or self.count_columns != other.count_lines:
            print('Матрицы нельзя умножить,т.к. кол-во эл. в столбце 1-ой матрицы, не соотв. кол-ву строк эл. во 2-ой')
        else:
            for i in range(self.count_lines):
                for j in range(other.count_columns):
                    for k in range(self.count_columns):
                        list_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                print(list_matrix[i])
            return list_matrix

    def transpositionMatrix(self):
        list_matrix = [[0 * i * j for j in range(self.count_lines)] for i in range(self.count_columns)]
        for i in range(self.count_columns):
            for j in range(self.count_lines):
                list_matrix[i][j] = self.matrix[j][i]
            print(list_matrix[i])

    def exponentiationMatrix(self):
        num = Expectation.int_expect()
        if self.count_lines == self.count_columns:
            other = copy.copy(self)
            for i in range(num - 1):
                print(f"{i + 1}-й шаг:")
                other.matrix = self*other
            print("Результат возведения в степень")
            other.showMatrix()
        else:
            print("Чтобы возвести матрицу в степень, она должна быть квадратной!")

    def writeMatrixToFile(self):
        file_name = open(f"{random.randint(0, 10000)} matrix.txt", 'a')
        for i in range(self.count_lines):
            for j in range(self.count_columns):
                file_name.write(str(self.matrix[i][j]) + ' ')
            file_name.write('\n')
        file_name.close()

# наш скрипт


if __name__ == '__main__':
    Menu.ActionMenu()
