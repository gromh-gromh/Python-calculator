import math
import configparser
from string import ascii_uppercase
from .calc_logging import write_log


def main():
    print('Добро пожаловать в очередной калькулятор')

    global PARAMS

    load_params()

    is_opened = True
    while is_opened:
        mode = input('Введите режим работы калькулятора (basics / array / help / exit): ')
        is_opened = select_mode(mode)

    input('Нажмите Enter чтобы выйти')

#Функция выбора режима работы калькулятора
def select_mode(mode):
    if mode == 'basics':
        print('Вы выбрали режим арифметических действий с двумя числами')
        operand1 = float(input("Введите операнд 1: "))
        operand2 = float(input("Введите операнд 2: "))

        act = input("Введите действие: ")

        r = calculate(operand1, operand2, act)
        print_calc(operand1, operand2, act = act, result = r, mode = mode)
        write_log(operand1, operand2, act = act, result = r, dest = PARAMS['dest'], output_type = PARAMS['output_type'])

        return True
    elif mode == 'array':
        print('Вы выбрали режим действий с массивом')

        n = int(input("Введите размер массива: "))
        array = []
        print("Введите массив: ")
        for i in range(0, n):
            array.append(float(input()))

        act = input("Введите действие: ")

        r = array_calculate(array = array.copy(), act = act)
        print_calc(*array, act = act, result = r, mode = mode)
        write_log(array, act = act, result = r, dest = PARAMS['dest'], output_type = PARAMS['output_type'])

        return True
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
        print('|--- n_min поиск наименьшего произведения n элементов массива')

        return True
    elif mode == 'exit':
        return False
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
            result = round(op1 / op2, convert_precision(PARAMS['precision']))
        else:
            result = 'деление на ноль невозможно'
    elif act == '^':
        if op2 % 1 == 0:
            result = op1**op2
        else:
            result = 'Невозможно возвести в нецелую степень'
    elif act == 'log':
        if op2 > 0:
            result = round(math.log(op1, op2), convert_precision(check_params(PARAMS['precision'])))
        else:
            result = 'Неправильное основание логарифма'
    else:
        result = 'такой операции нет'

    return result

#Функция с действиями с массивами
def array_calculate(array, act):
    if act == 'std_dev':
        result = standart_deviation(*array, precision = PARAMS['precision'])
    elif act == 'two_sum':
        result = two_sum(*array)
    elif act == 'n_min':
        n = int(input('Введите количество чисел в искомом произведении '))
        result = n_min(lst = array, n = n)
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

#Функция для поиска наименьших элементов массива
def n_min(lst = [], n = 1):
    lst.sort()
    temp_min_1 = temp_min_2 = lst[0]

    for i in range(1, n):
        temp_min_1 *= lst[i]
    for i in range(len(lst) - 1, len(lst) - n, -1):
        temp_min_2 *= lst[i]

    n_min = min(temp_min_1, temp_min_2)

    return n_min  


#Функция для конвертации значения точности из float в int
def convert_precision(precision=None):
    if type(precision) is float:
        precision = format(precision, '.5f')
    for i in range(len(str(precision))):
        if float(precision) * 10**i >= 1:
            return i

#Функция для загрузки параметров
def load_params():
    print('Загрузка параметров...')

    config = configparser.ConfigParser()
    config.read('params.ini')
    params_tuples_list = config.items('DEFAULT')

    global PARAMS
    PARAMS = {i[0] : i[1] for i in params_tuples_list}

    check_params()

    print('Параметры загружены:')    
    print(PARAMS)


#Функция для проверки параметров
def check_params():
    global PARAMS
    try:
        PARAMS['precision'] = float(PARAMS['precision'])
    except  Exception:
        PARAMS['precision'] = '0.00001'

    if PARAMS['output_type'] == '':
        PARAMS['output_type'] = '.txt'
        
    if PARAMS['dest'] == '':
        PARAMS['dest'] = 'calc_log'

#Функция для табличного вывода результатов
def print_calc(*args, act = None, result = None, mode = None):
    raw_table = []
    row_1 = []
    row_2 = []
    expression = ""

    #Формирование массива, репрезентующего абстракцию таблицы
    for i in range(0, len(args)):
        row_1.append(ascii_uppercase[i])
        row_2.append(args[i])
    
    if(mode == "array"):
        expression = f"{act}("
        for i in range(0, len(row_1)):
            expression += f"{row_1[i]}, "
        expression = expression[:-2] + ")"
    if(mode == "basics"):
        for i in range(0, len(row_1)):
            expression += f"{row_1[i]} {act} "
        expression = expression[:-3]

    row_1.append(expression)
    row_2.append(result)
    raw_table = [row_1, row_2]

    #Приведение массива к табличному виду
    formated_row_1 = ""
    formated_row_2 = ""

    for i in range(0, len(raw_table[0])):
        if(len(str(raw_table[0][i])) > len(str(raw_table[1][i]))):
            cell_1 = f"* {raw_table[0][i]} "
            whitespace_length = (len(cell_1) - 1 - len(str(raw_table[1][i])))
            cell_2 = "*" + " " * int(whitespace_length / 2) + str(raw_table[1][i]) + " " * (whitespace_length - int(whitespace_length / 2))
        else:
            cell_2 = f"* {raw_table[1][i]} "
            whitespace_length = (len(cell_2) - 1 - len(str(raw_table[0][i])))
            cell_1 = "*" + " " * int(whitespace_length / 2) + str(raw_table[0][i]) + " " * (whitespace_length - int(whitespace_length / 2))
        formated_row_1 += cell_1
        formated_row_2 += cell_2
    formated_row_1 += "*"
    formated_row_2 += "*"

    #Вывод полученной таблицы
    print("*" * len(formated_row_1))
    print(formated_row_1)
    print("*" * len(formated_row_1))
    print(formated_row_2)
    print("*" * len(formated_row_1))

if __name__ == "__main__":
    main()
