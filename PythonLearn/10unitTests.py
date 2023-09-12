import unittest

#Class that inherits from unittest.TestCase
class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
        
def add(*args):
    return sum(args)

if __name__ == '__main__':
    unittest.main()
