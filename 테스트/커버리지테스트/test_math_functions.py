import unittest
from math_functions import add, subtract, multiply, divide

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertRaises(ValueError, divide, 1, 0)

if __name__ == '__main__':
    unittest.main()

# 해당 경로 터미널에서 coverage run -m unittest test_math_functions.py      - 테스트를 실행하고, 커버리지를 측정
# 해당 경로 터미널에서 coverage html        - 좀 더 보기 좋은 HTML 리포트를 생성
# 해당 경로 터미널에서 coverage report      - 커맨드라인에서 커버리지 리포트를 텍스트 형식으로 출력
