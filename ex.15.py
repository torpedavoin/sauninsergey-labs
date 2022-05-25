"""15. Дано координати (x; y) точки і радіус кола (r). Визначити чи належить дана точка колі, якщо його
центр знаходиться на початку координат."""


import math


def main(x: float, y: float ,r: float):
    h = math.sqrt(x ** 2 + y ** 2)
    if h <= r:
        return f'Належить колу'
    else:
        return f'Не належить колу'


if __name__ == '__main__':
    _x = float(input("Введіть X "))
    _y = float(input("Введіть Y "))
    _r = float(input("Введіть R "))
    result = main(_x, _y, _r)
    print(result)