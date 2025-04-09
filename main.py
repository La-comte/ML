class My_matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.det = 0
        self.matrix = [[0] * row for _ in range(column)]

    def input_my(self):
        for r in range(self.row):
            for c in range(self.column):
                self.matrix[r][c] = int(input())
        if self.row == self.column:
            self.det_my()

    def det_my(self):
        if self.row == 2:
            self.det = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            self.det = determinant(self.matrix)

    def enter_my(self):
        for r in range(self.row):
            for c in range(self.column):
                print(str(self.matrix[r][c]).ljust(3), end='')
            print()

    def enter_main(self):
        print('Основная диагональ')
        for i in range(self.row):
            print(self.matrix[i][i], ' ')
        print('Побочная диагональ')
        for i in range(self.row):
            print(self.matrix[self.row - i - 1][i], ' ')


def determinant(matrix):
    det = 0
    for i in range(3):
        minor = matrix[1][(i + 1) % 3] * matrix[2][(i + 2) % 3] - matrix[1][(i + 2) % 3] * matrix[2][(i + 1) % 3]
        if i == 2:
            det -= matrix[0][i] * minor
        else:
            det += matrix[0][i] * minor
    return det


def multiplication(my_matrix, new_matrix):
    t = my_matrix.row
    n = new_matrix.column
    m = new_matrix.row
    multi_matrix = My_matrix(t, n)
    matrix = [[0] * t for _ in range(n)]
    for i in range(t):
        for j in range(n):
            c = 0
            for r in range(m):
                c += my_matrix.matrix[i][r] * new_matrix.matrix[r][j]
            matrix[i][j] = c
    multi_matrix.matrix = matrix
    return multi_matrix


print('Добро пожаловать! Выберите размер квадратной матрицы: 1)2х2, 2)3х3')
if input() == '1':
    my_matrix = My_matrix(2, 2)
else:
    my_matrix = My_matrix(3, 3)

action = '1'

while action in '1234567':
    print('Выберите действие:' +
          '\n\t1)Выбрать размер квадратной матрицы: 2х2, 3х3' +
          '\n\t2)Ввод элементов матрицы' +
          '\n\t3)Получение значения определителя' +
          '\n\t4)Проверка является ли матрица вырожденной или невырожденной;' +
          '\n\t5)Вывод элементов главной и побочной диагоналей матрицы' +
          '\n\t6)Вывод элементов матрицы' +
          '\n\t7)умножить матрицу на другую')
    action = input()
    match action:
        case '1':
            print('\tВыберите размер квадратной матрицы: 1)2х2, 2)3х3')
            if input() == '1':
                my_matrix = My_matrix(2, 2)
            else:
                my_matrix = My_matrix(3, 3)
        case '2':
            my_matrix.input_my()
        case '3':
            print(my_matrix.det)
        case '4':
            if my_matrix.det == 0:
                print('\tМатрица вырождена')
            else:
                print('\tМатрица не вырождена')
        case '5':
            my_matrix.enter_main()
        case '6':
            my_matrix.enter_my()
        case '7':
            print('\tВведите количество строк и столбцов матрицы')
            new_matrix = My_matrix(int(input()), int(input()))
            if my_matrix.column != new_matrix.row:
                print('\tТакие матрицы невозможно умножить')
                continue
            print('\tВведите матрицу')
            new_matrix.input_my()
            multi = multiplication(my_matrix, new_matrix)
            multi.enter_my()