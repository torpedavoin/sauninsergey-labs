"""20. Присвоїти цілій змінній d першу цифру з дробової частини позитивного дійсного числа x"""


def main(x: float):
    """Function of searching first number after dot"""
    if x > 0:
        d = x * 10 % 10
    else:
        print("Error")
    return f'D = {int(d)}'


if __name__ == '__main__' :
    _x = float(input("Enter x: "))
    result = main(_x)
    print(result)
