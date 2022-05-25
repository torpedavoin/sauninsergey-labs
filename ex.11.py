"""11. Дано три змінні: X, Y, Z. Якщо їх значення впорядковані за спаданням, то подвоїти їх; в іншому
випадку замінити значення кожної змінної на протилежне"""


def main(x: float, y: float, z: float):
    if x > y and y > z:
        return f'New Y ={x * 2}\nNew Y ={y * 2}\nNew Z ={z * 2}'
    else:
        return f'New Y = {x * -1}\nNew Y = {y * -1}\nNew Z = {z * -1}'


if __name__ == '__main__':
    _x = float(input("Enter X "))
    _y = float(input("Enter Y "))
    _z = float(input("Enter Z "))
    result=main(_x, _y, _z)
    print(result)