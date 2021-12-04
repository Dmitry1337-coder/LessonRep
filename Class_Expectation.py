from abc import ABC


class Expectation(ABC):

    @staticmethod
    def int_expect():
        while True:
            try:
                value = int(input())
                break
            except ValueError:
                print("Требуется ввести число цифрами(без пробелов, запятых и иных символов)!")
        return value

    @staticmethod
    def str_expect():
        while True:
            try:
                value = str(input()).split()[0]
                break
            except ValueError:
                print("Требуется символьное значение!")
        return value

    @staticmethod
    def list_expect(len_list):
        while True:
            try:
                list_values = str(input()).split()
                if len(list_values) == len_list:
                    list_values = [int(el) for el in list_values]
                else:
                    raise ValueError
                break
            except ValueError:
                print("Требуется ввести строку из целых чисел через пробел!")
                print(f"Количество элементов в строке должно быть равно: {len_list}")
        return list_values
