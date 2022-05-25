"""5. Обчислити дробову частину середнього геометричного трьох заданих позитивних чисел."""


import math


def main(a: float, b: float, c: float):
    """Function of finding fraction of average geometric of three numbers"""
    if a > 0 and b > 0 and c > 0:
        x = (a * b * c) ** (1/3)
        return f'X = {x-math.floor(x)}'
    else:
        return "Error"


if __name__ == '__main__':
    _a = float(input("Enter first number "))
    _b = float(input("Enter second number "))
    _c = float(input("Enter third number "))
    result = main(_a, _b, _c)
    print(result)