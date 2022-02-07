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
