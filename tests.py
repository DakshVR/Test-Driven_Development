import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    # Password with length less then 8
    def test1(self):
        input = '123gt6'
        self.assertFalse(check_pwd(input))

    # Password with length more than 20, length 22
    def test2(self):
        input = 'at567yhjuliokjuy6785ft'
        self.assertFalse(check_pwd(input))

    # Password with no lowercase character should Fail
    def test3(self):
        input = 'ASDFGHIP'
        self.assertFalse(check_pwd(input))

    # Password with no uppercase character should Fail
    def test5(self):
        input = 'erqyuiolkp'
        self.assertFalse(check_pwd(input))

    # Password with no digit should Fail
    def test7(self):
        input = 'rtyuijkuUIO'
        self.assertFalse(check_pwd(input))

    # Password with no symbols should Fail
    def test8(self):
        input = 'Asgt67hU89'
        self.assertFalse(check_pwd(input))

    # Password with lower case, upper case and symbol should Fail, no digit
    def test9(self):
        input = 'akshUY@O+'
        self.assertFalse(check_pwd(input))

    # Password with all criteria met, should return True
    def test10(self):
        input = '@3*UYhj89'
        self.assertTrue(check_pwd(input))

    # Password with upper case, digit and symbol should Fail, no lowercase character
    def test11(self):
        input = 'WERT657&@E'
        self.assertFalse(check_pwd(input))


if __name__ == '__main__':
    unittest.main()
