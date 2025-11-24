import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('Start testing a silly function')

    def test_do_stuff(self):
        '''The first test'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'test'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def tearDown(self):
        print('Finish testing a silly function')

if __name__ == '__main__':
    unittest.main()
