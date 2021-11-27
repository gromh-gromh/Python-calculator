from main import calculate

def test_sum():
    assert calculate(1, 2, '+') == 3, "Неправильная сумма"


def test_subtraction():
    assert calculate(2, 1, '-') == 1, "Неправильная разность"


def test_multiplication():
    assert calculate(2, 3, "*") == 6, "Неправильное умножение"


def test_division():
    assert calculate(
        3, 0, "/"
    ) == 'деление на ноль невозможно', "Проверка равенства делителя нулю"


def test_power():
    assert calculate(
        2, 2.1, "power"
    ) == 'Невозможно возвести в нецелую степень', "Проверка принадлежности показателя степени к целым числам"


def test_log():
    assert calculate(
        2, -1, "log"
    ) == 'Неправильное основание логарифма', "Проверка положительности основания логарифма"