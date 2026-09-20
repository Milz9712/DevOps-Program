import unittest

from health_utils import check_threshold


class TestHealthUtils(unittest.TestCase):

    def test_value_below_threshold(self):
        self.assertEqual(check_threshold(50, 80), "OK")

    def test_value_at_threshold(self):
        self.assertEqual(check_threshold(80, 80), "WARNING")

    def test_value_above_threshold(self):
        self.assertEqual(check_threshold(90, 80), "WARNING")

    def test_value_zero(self):
        self.assertEqual(check_threshold(0, 80), "OK")


if __name__ == "__main__":
    unittest.main()