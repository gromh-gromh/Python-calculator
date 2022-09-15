#Функция для вывода логов вычислений
def write_log(*args, act = None, result, dest, output_type):
    file = open(dest + output_type, mode = 'a', errors = 'ignore')

    file.write(f"{act} : {args} = {result} \n")
    file.close()