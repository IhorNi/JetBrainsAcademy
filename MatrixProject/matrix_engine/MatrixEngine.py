class Matrix:

    def __init__(self, user_input):

        init = user_input.split()

        if len(init) == 1:
            self.rows = 1
            self.cols = 1
        else:
            self.rows = int(init[0])
            self.cols = int(init[1])

        self.result = []
        for x in range(self.rows):
            temp = input()
            if '.' in temp:
                row = list(map(float, temp.split()))
                self.result.append(row)
            else:
                row = list(map(int, temp.split()))
                self.result.append(row)

    def transpose(self, chosen_method):

        # 1. Main diagonal, 2. Side diagonal, 3. Vertical line, 4. Horizontal line
        if chosen_method == "1":
            result = [[self.result[x][y] for x in range(len(self.result))] for y in range(len(self.result[0]))]
        elif chosen_method == "2":
            result = [[self.result[x][y] for x in range(len(self.result))] for y in
                      range(len(self.result[0]) - 1, -1, -1)]
            result = [x[::-1] for x in result]
        elif chosen_method == "3":
            result = [x[::-1] for x in self.result]
        elif chosen_method == "4":
            result = self.result[::-1]
        for line in result:
            row = " ".join([str(num) for num in line])
            print(row)

def getcofactor(matrix, i, j):

    return [row[: j] + row[j + 1:] for row in (matrix[: i] + matrix[i + 1:])]


def determinant(matrix):
    """Function to recursively calculate matrix determinant"""

    if len(matrix) == 1:
        value = matrix[0][0]
        return value

    if len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value

    sum = 0
    for current_column in range(len(matrix)):
        sign = (-1) ** current_column
        sub_det = determinant(getcofactor(matrix, 0, current_column))
        sum += (sign * matrix[0][current_column] * sub_det)

    return sum


def get_inverse_matrix(matrix):
    """Function to calculate inverse matrix if possible"""

    det = determinant(matrix)
    # special case for 2x2 matrix:
    if det != 0:
        if len(matrix) == 2:
            return [[matrix[1][1] / det, -1 * matrix[0][1] / det],
                    [-1 * matrix[1][0] / det, matrix[0][0] / det]]

        # find matrix of cofactors
        cofactors = []
        for r in range(len(matrix)):
            cofactorRow = []
            for c in range(len(matrix)):
                minor = getcofactor(matrix, r, c)
                cofactorRow.append(((-1) ** (r + c)) * determinant(minor))
            cofactors.append(cofactorRow)
        cofactors = list(map(list, zip(*cofactors)))

        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / det

        for line in cofactors:
            row = " ".join([str(num) for num in line])
            print(row)
    else:
        print("This matrix doesn't have an inverse.")


def multiply_by_number(matrix, number):
    """Function to multiply matrix by number"""

    for i in range(matrix.rows):
        temp = []
        for j in range(matrix.cols):
            temp.append(str(matrix.result[i][j] * number))
        print(' '.join(temp))


def matrix_dot_product(matrix_1, matrix_2):
    """Dot product of Matrix class objects"""

    result = []
    for _ in range(matrix_1.rows):
        result.append([0 for _ in range(matrix_2.cols)])

    if matrix_1.cols == matrix_2.rows:
        for i in range(len(matrix_1.result)):
            for j in range(len(matrix_2.result[0])):
                for k in range(len(matrix_2.result)):
                    result[i][j] += matrix_1.result[i][k] * matrix_2.result[k][j]
    for i in range(len(result)):
        print(" ".join([str(num) for num in result[i]]))
    else:
        print("The operation cannot be performed.")


def matrix_sum(matrix_1, matrix_2):
    """Function to perform matrix sum"""

    if (matrix_1.rows == matrix_2.rows) and (matrix_1.cols == matrix_2.cols):
        for x in range(matrix_1.rows):
            add_result = [matrix_1.result[x][y] + matrix_2.result[x][y] for y in range(matrix_1.cols)]
            print(" ".join([str(num) for num in add_result]))
    else:
        print("The operation cannot be performed.")


def safe_option_input(lower_bound, upper_bound):
    """Function to safely read input option"""

    try:
        option = int(input("Your choice: "))
        if option < lower_bound or option > upper_bound:
            print('No such operation\n')
            print(f'Please, choose option from {lower_bound} to {upper_bound}')
            return None
        else:
            return option
    except ValueError:
        print('\nPlease, enter number from 0 to 4')
        return None


def matrix_calculator():
    """Matrix calculator app"""

    MENU = ['1. Add matrices',
            '2. Multiply matrix by a constant',
            '3. Multiply matrices',
            '4. Transpose matrix',
            '5. Calculate a determinant',
            '6. Inverse matrix',
            '0. Exit']

    MENU_TRANSPOSE = ['1. Main diagonal',
                      '2. Side diagonal',
                      '3. Vertical line',
                      '4. Horizontal line']

    while True:

        print('\n'.join(MENU))

        option = safe_option_input(0, 6)
        if option is None:
            continue
        if option == 0:
            break

        if option == 1:
            matrix_1 = Matrix(input("Enter size of first matrix:"))
            matrix_2 = Matrix(input("Enter size of second matrix:"))
            print('The result is:')
            matrix_sum(matrix_1, matrix_2)
        elif option == 2:
            matrix = Matrix(input("Enter size of matrix:"))
            constant = int(input('Enter constant:'))
            print('The result is:')
            multiply_by_number(matrix, constant)
        elif option == 3:
            matrix_1 = Matrix(input("Enter size of first matrix:"))
            matrix_2 = Matrix(input("Enter size of second matrix:"))
            print('The result is:')
            matrix_dot_product(matrix_1, matrix_2)
        elif option == 4:
            print('\n'.join(MENU_TRANSPOSE))
            option = safe_option_input(1, 4)
            matrix = Matrix(input("Enter size of matrix:"))
            print('The result is:')
            matrix.transpose(option)
        elif option == 5:
            matrix = Matrix(input("Enter size of matrix:"))
            print('The result is:')
            print(determinant(matrix.result))
        else:
            matrix = Matrix(input("Enter size of matrix:"))
            print('The result is:')
            get_inverse_matrix(matrix.result)



