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

    # Password with one lowercase character should pass
    def test4(self):
        input = 'aWRSTYUIP'
        self.assertTrue(check_pwd(input))

    # Password with no uppercase character should Fail
    def test5(self):
        input = 'erqyuiolkp'
        self.assertFalse(check_pwd(input))

    # Password with one uppercase character and one lower case character, should Pass
    def test6(self):
        input = '12345t78U8'
        self.assertTrue(check_pwd(input))


if __name__ == '__main__':
    unittest.main()
