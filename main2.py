from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Выводит сообщение с результатом вычислений."""
    result = calculate_square_root(your_number)
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами '
          f'числа. Это будет: {result}')


print(message)
calc(25.5)
