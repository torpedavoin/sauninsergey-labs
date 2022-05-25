"""10. Даний розмір файла в байтах. Використовуючи операцію ділення без залишку, знайти кількість
повних кілобайтів, які займає даний файл (1 кілобайт = 1024 байта)"""


import math


num_b = int(input("Enter the size in bytes : "))


if num_b > 0:
    num_kb = num_b/1024
    print("Size in kilobytes", int(num_kb))
else:
    print("Error")
