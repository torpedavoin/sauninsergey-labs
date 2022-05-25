"""5. Дано ціле число. Вивести його рядок-опис виду «від'ємне парне число», «нульове число», «додатне
непарне число» і т. д"""


def main(num):
    if num == 0:
        return f'нульове число'
    elif num % 2 == 0:
        print("парне")
    else:
        print("непарне")
    if num > 0:
        return f'додатнє'
    else:
        return f'відємне'


if __name__ == '__main__':
    n = int(input("Введите число "))
    result = main(n)
    print(result)
