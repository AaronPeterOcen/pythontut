import unittest
import main


class TestMain(unittest.TestCase):
    def test_stuff(self):
        test_param = 10
        result = main.stuff(test_param)
        self.assertEqual(result, 13)

    def test_stuff2(self):
        test_param = "saklaka"
        result = main.stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))


unittest.main()
