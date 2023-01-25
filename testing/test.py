import unittest
import script


class TestGame(unittest.TestCase):
    def test_input_right_guess(self):
        result = script.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = script.run_guess(5, 3)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = script.run_guess(12, 4)
        self.assertFalse(result)

    def test_input_wrong_input(self):
        result = script.run_guess('ls', 4)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
