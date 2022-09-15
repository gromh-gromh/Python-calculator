#calculate
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

 #convert_precision
import unittest
from main import convert_precision


class TestPrecisionFunc(unittest.TestCase):
    def test_norm_vals(self):
        self.assertEqual(convert_precision(0.000001), 6)
        self.assertEqual(convert_precision(0.0001), 4)

    def test_convertable_inp_value(self):
        self.assertEqual(convert_precision("0.000001"), 6)

    def test_type_error_raises(self):
        with self.assertRaisesRegex(TypeError, 'неверный тип аргумента'):
            convert_precision('0.000001a')


unittest.main(verbosity=1)

#two_sum
from main import two_sum
import unittest

class TestPrecisionFunc(unittest.TestCase):
    def test_norm_vals(self):
        self.assertEqual(two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 8), (0, 6))
        self.assertEqual(two_sum([1, 1, 2, 3], 2), (0, 1))

    def test_duplicated_vals(self):
        self.assertEqual(two_sum([1, 1, 1, 1], 2), (0, 1))
        self.assertEqual(two_sum([1, 0, 0, 1], 2), (0, 3))

    def test_target_sum_not_found(self):
        self.assertIsNone(two_sum([1, 2, 3, 4], 8))


unittest.main(verbosity=1)