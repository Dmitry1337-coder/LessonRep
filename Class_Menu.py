from abc import ABC

from Class_Matrices import Matrices
from Class_Expectation import Expectation


def list_output(list_):
    if isinstance(list_, list):
        for i in list_:
            print(i)


class Menu(ABC):
    action = int

    @staticmethod
    def MainMenu():
        print("1. Сложение матриц")
        print("2. Вычитание матриц")
        print("3. Умножение матриц")
        print("4. Транспонирование матриц")
        print("5. Умножение матриц на число")
        print("6. Возведение матрицы в степень")
        print("0. Выход")

    # size_matrix = [<кол-во строк>,<кол-во столбов>]
    @staticmethod
    def InputMatrix():
        object_matrix = object
        while True:
            try:
                print("Введите размер матрицы: <кол-во_строк> <кол-во_столбцов>:")
                size_matrix = Expectation.list_expect(2)
                count_lines = size_matrix[0]
                count_columns = size_matrix[1]
                if (count_lines == 0 and count_columns != 0) or \
                        (count_columns == 0 and count_columns != 1) or \
                        (count_lines == count_columns == 0):
                    raise ValueError
                if count_lines*count_columns >= 30:
                    print("Размер матрицы слишком велик. Правильно ли вы ввели данные?(y/n)")
                    if Expectation.str_expect() != 'y':
                        print("Попробуйте снова!")
                        continue
                object_matrix = Matrices(count_lines, count_columns)
                object_matrix.writeMatrix()
                break
            except ValueError:
                print("Введите размер матрицы снова, т.к. один из размеров равен нулю.")
        return object_matrix

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
            elif action == 6:
                Menu.actionExponentiation()
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
        print("Введите матрицы, которые будут сложены:")
        matrix1 = Menu.InputMatrix()
        matrix2 = Menu.InputMatrix()
        matrix1 + matrix2

    @staticmethod
    def actionSubtraction():
        print("Введите матрицы, которые будут вычитаться:")
        matrix1 = Menu.InputMatrix()
        matrix2 = Menu.InputMatrix()
        matrix1 - matrix2

    @staticmethod
    def actionMultiplication():
        print("Введите матрицы, которые умножатся друг на друга:")
        matrix1 = Menu.InputMatrix()
        matrix2 = Menu.InputMatrix()
        multiplication = matrix1 * matrix2
        list_output(multiplication)

    @staticmethod
    def actionTranspose():
        print("Введите матрицу для транспонирования:")
        matrix = Menu.InputMatrix()
        matrix.transpositionMatrix()

    @staticmethod
    def actionMulConstant():
        print("Введите матрицу, которая умножится на число:")
        matrix = Menu.InputMatrix()
        print("Введиет число, на которое уможается матрица:")
        number = Expectation.int_expect()
        matrix.mulOnConstant(number)

    @staticmethod
    def actionExponentiation():
        print("Введите матрицу, которая будет возведена в степень")
        matrix = Menu.InputMatrix()
        print("Введите степень возводимой матрицы:")
        number = Expectation.int_expect()
        list_output(matrix.exponentiationMatrix(number))
