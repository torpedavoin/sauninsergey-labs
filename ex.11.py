"""11. Знайти значення функції y=3x^6+6x^2+7 при даному значенні x."""


import math


def main(x: float):
    y = 3 * x ** 6 + 6 * x ** 2 + 7
    return f'Answer {y}'


if __name__ == '__main__':
    _x = float(input("Enter X "))
    result = main(_x)
    print(result)