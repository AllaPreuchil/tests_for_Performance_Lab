import unittest
import task1


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        result = task1.get_route(['', '4', '3'])
        self.assertEqual('13', result)

    def test_case2(self):
        result = task1.get_route(['', '5', '4'])
        self.assertEqual('14253', result)


if __name__ == '__main__':
    unittest.main()
