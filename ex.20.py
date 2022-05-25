"""20. Дано ціле число, яке лежить в діапазоні 1-999. Вивести його рядок-опис виду «парне двозначне
число», «непарне тризначне число» і т. Д"""


def main(num: int):
    if num < 1000 and num > 1:
            if num % 2 == 0:
                print("четное")
            else:
                print("нечетное")
            if num >= 100 and num < 1000:
                return f'трехзначное'
            elif num < 100 and num >= 10:
                return f'двухзначное'
            elif num < 10 and num >= 1:
                return f'однозначное'
    else:
        return f'Error'

if __name__ == '__main__':
    n = int(input("Введите число от 1 до 999 "))
    result = main(n)
    print(result)