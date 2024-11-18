# 코드 커버리지 측정 예시
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

import unittest


class TestDivision(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertRaises(ValueError, divide, 6, 0)

if __name__ == "__main__":
    unittest.main()
