import math
import configparser


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
        print("Результат: ", r)
        write_log(operand1, operand2, act = act, result = r)

        return True
    elif mode == 'array':
        print('Вы выбрали режим действий с массивом')

        n = int(input("Введите размер массива: "))
        array = []
        print("Введите массив: ")
        for i in range(0, n):
            array.append(float(input()))

        act = input("Введите действие: ")

        r = array_calculate(*array, act = act)
        write_log(array, act = act, result = r)
        print("Результат: ", r)

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
def array_calculate(*array, act):
    if act == 'std_dev':
        result = standart_deviation(*array, precision = check_params(PARAMS['precision']))
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

#Функция для вывода логов вычислений
def write_log(*args, act = None, result):
    file = open(PARAMS['dest'] + PARAMS['output_type'], mode = 'a', errors = 'ignore')

    file.write(f"{act} : {args} = {result} \n")
    file.close()
 

main()
