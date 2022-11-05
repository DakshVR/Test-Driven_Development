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


if __name__ == '__main__':
    unittest.main()
