import math


def main():
    print('Добро пожаловать в очередной калькулятор')
    while True:
        mode = input('Введите режим работы калькулятора (basics / array / help): ')
        select_mode(mode)

#Функция выбора режима работы калькулятора
def select_mode(mode):
    if mode == 'basics':
        print('Вы выбрали режим арифметических действий с двумя числами')
        operand1 = float(input("Введите операнд 1: "))
        operand2 = float(input("Введите операнд 2: "))

        act = input("Введите действие: ")

        r = calculate(operand1, operand2, act)
        print("Результат: ", r)
    elif mode == 'array':
        print('Вы выбрали режим действий с массивом')

        n = int(input("Введите размер массива: "))
        array = []
        print("Введите массив: ")
        for i in range(0, n):
            array.append(float(input()))

        act = input("Введите действие: ")

        r = array_calculate(*array, act = act)
        print("Результат: ", r)
    elif mode == 'help':
        print('Список доступнух действий:')
        print('|Режим арифметических действий с двумя числами:')
        print('|--- + сложение')
        print('|--- - вычитание')
        print('|--- * умножение')
        print('|--- / деление')
        print('|--- ^ возведение в степень')
        print('|--- log логарифмирование')
        print('|Режим действий с массивом')
        print('|--- std_dev среднеквадратическое отклонение')
        print('|--- two_sum поиск индексов пар чисел, сумма которых равна заданному числу')
    else:
        print('Такого режима нет')

#Функция с арифмитическими действиями с двумя числами
def calculate(op1, op2, act): 
    if act == '+':
        result = op1 + op2
    elif act == '-':
        result = op1 - op2
    elif act == '*':
        result = op1 * op2
    elif act == '/':
        if op2 != 0:
            settings = precision_input()
            result = round(op1 / op2, convert_precision(load_params(**settings)))
        else:
            result = 'деление на ноль невозможно'
    elif act == '^':
        if op2 % 1 == 0:
            result = op1**op2
        else:
            result = 'Невозможно возвести в нецелую степень'
    elif act == 'log':
        if op2 > 0:
            settings = precision_input()
            result = round(math.log(op1, op2), convert_precision(load_params(**settings)))
        else:
            result = 'Неправильное основание логарифма'
    else:
        result = 'такой операции нет'

    return result

#Функция с действиями с массивами
def array_calculate(*array, act):
    if act == 'std_dev':
        settings = precision_input()
        result = standart_deviation(*array, precision = load_params(**settings))
    elif act == 'two_sum':
        result = two_sum(*array)
    else:
        result = 'Такой операции нет'
        
    return result

#Функция для вычисления среднеквадратического отклонения
def standart_deviation(*args, precision = None):
    mean = sum(args) / len(args)

    delta = []
    for x in args:
        delta.append(x - mean)

    dispersion = 0
    for x in delta:
        dispersion += x**2
    dispersion /= len(delta)

    std_deviation = round(math.sqrt(dispersion), convert_precision(precision))

    return std_deviation

#Функция для поиска двух элементов массива, сумма которых равна target
def two_sum(*lst):
    target = float(input('Введите искомое значение суммы: '))
    pairs = []
    pair = tuple()

    dict = {target - lst[i]: i for i in range(0, len(lst))}
    
    for i in range(0, len(lst) // 2):
        if i != dict[lst[i]]:
            pair = (i, dict[lst[i]])
            pairs.append(pair)
    return pairs  

#Функция ввода точности вычислений
def precision_input():
    print('Введите точность выбранного вычисления')
    precision = input()
    settings = {'precision': precision}
    return settings

#Функция для конвертации значения точности из float в int
def convert_precision(precision=None):
    if type(precision) is float:
        precision = format(precision, '.5f')
    for i in range(len(str(precision))):
        if float(precision) * 10**i >= 1:
            return i

#Функция для загрузки параметров
def load_params(**kwargs):
    precision = kwargs['precision']
    try:
        precision = float(precision)
    except  Exception:
        precision = '0.00001'

    return precision
 

main()
