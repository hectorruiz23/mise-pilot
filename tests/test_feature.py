import unittest


def double(value):
    return value * 2


class Feature(unittest.TestCase):
    def test_doubles(self):
        self.assertEqual(double(2), 5)


if __name__ == "__main__":
    unittest.main()
