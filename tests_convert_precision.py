from main import convert_precision

def test_cp_with_1():
  assert convert_precision('0.1') == 1, "Должна быть 1"


def test_cp_with_2():
  assert convert_precision('0.01') == 2, "Должно быть 2"


def test_cp_with_5():
  assert convert_precision('0.00001') == 5, "Должно быть 5"


def test_cp_with_5_as_float():
  assert convert_precision(0.00001) == 5, "Должно быть 5"