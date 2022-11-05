import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    # Password with length less then 8
    def test1(self):
        input = '123gt6'
        self.assertFalse(check_pwd(input))


if __name__ == '__main__':
    unittest.main()
