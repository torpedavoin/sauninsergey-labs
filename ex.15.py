"""15. Дано змінні A, B, C. Змінити їх значення, перемістивши вміст A в B, B - в C, C - в A, і вивести
нові значення змінних A, B, C."""


def main(a: float, b: float, c: float):
    """The function of switching A>B,B>C,C>A"""
    a, b, c = b, c, a
    return f'New A = {a}\nNew B = {b}\nNew C = {c}'


if __name__ == '__main__' :
    _a = input("Enter A ")
    _b = input("Enter B ")
    _c = input("Enter C ")
    result = main(_a, _b, _c)
    print(result)

