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

    ######## Partner 1
     def test_multiply(self): # 3 assertions
         self.assertEqual(mul(3, 4), 12)
         self.assertEqual(mul(-2, 5), -10)
         self.assertEqual(mul(0, 100), 0)

     def test_divide(self): # 3 assertions
         self.assertEqual(div(2, 10), 5)
         self.assertAlmostEqual(div(4, 1), 0.25)
         self.assertEqual(div(1, 5), 5)


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
     def test_log_invalid_argument(self): # 1 assertion
         with self.assertRaises(ValueError):
             logarithm(0, 5)

     def test_hypotenuse(self): # 3 assertions
         self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
         self.assertAlmostEqual(hypotenuse(0, 5), 5.0)
         self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

     def test_sqrt(self): # 3 assertions
         self.assertAlmostEqual(square_root(9), 3.0)
         self.assertAlmostEqual(square_root(0), 0.0)
         with self.assertRaises(ValueError):
             square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()