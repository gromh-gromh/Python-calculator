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