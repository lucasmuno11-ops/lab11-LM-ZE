import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
     def test_add(self): # 3 assertions
         self.assertEqual(add(2, 3), 5)
         self.assertEqual(add(-1, 1), 0)
         self.assertEqual(add(10, 5), 15)
    #     fill in code

     def test_subtract(self): # 3 assertions
         self.assertEqual(subtract(5, 3), 2)
         self.assertEqual(subtract(0, 4), -4)
         self.assertEqual(subtract(10, 10), 0)

    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
     def test_divide_by_zero(self): # 1 assertion
         with self.assertRaises(ZeroDivisionError):
             div(0, 5)
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code


     def test_logarithm(self): # 3 assertions
         self.assertEqual(logarithm(10, 100), 2)
         self.assertEqual(logarithm(2, 8), 3)
         self.assertEqual(logarithm(3, 9), 2)
    #     fill in code

     def test_log_invalid_base(self): # 1 assertion
         with self.assertRaises(ValueError):
             logarithm(1, 5)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()