import unittest
import main_test


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print('about to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = main_test.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'hgjhkl'
        result = main_test.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main_test.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main_test.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self) -> None:
        print('cleaning up')


if __name__ == '__main__':
    unittest.main
