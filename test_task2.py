""" Test for Task2: Checking the functionality in 'task2.py' using assertions """

import unittest
import math
import task2


class Test(unittest.TestCase):
    def test1_sample(self):
        x = task2.sample(5, 55, 11)
        self.assertAlmostEqual(x[0], 5.0, delta=1e-3)
        self.assertAlmostEqual(x[1], 10.0, delta=1e-3)
        self.assertAlmostEqual(x[2], 15.0, delta=1e-3)
        self.assertAlmostEqual(x[9], 50.0, delta=1e-3)
        self.assertAlmostEqual(x[10], 55.0, delta=1e-3)

    def test2_eval_range(self):
        v0 = 72/3.6    # km/h converted to m/s
        theta = 45 * math.pi/180   # degrees to rad
        range_expected = 40.77471967380224
        self.assertAlmostEqual(task2.eval_range(v0, theta), range_expected, delta=1e-2)

    def test3_eval_height(self):
        v0 = 72/3.6    # km/h converted to m/s
        theta = 45 * math.pi/180   # degrees to rad            
        x = [0.0, 10.0, 20.0, 30.0, 40.0]
        y_expected = [0.0, 7.5474999999999985, 10.189999999999998, 7.927499999999998, 0.759999999999998]

        y = []
        for xi in x:
            y.append(task2.eval_height(v0, theta, xi))

        for yi, yi_expected in zip(y, y_expected):
            self.assertAlmostEqual(yi, yi_expected, delta=1e-3)

    def test4_eval_height_vectorized(self):
        v0 = 72/3.6    # km/h converted to m/s
        theta = 45 * math.pi/180   # degrees to rad            
        x = [0.0, 10.0, 20.0, 30.0, 40.0]
        y_expected = [0.0, 7.5474999999999985, 10.189999999999998, 7.927499999999998, 0.759999999999998]

        y = task2.eval_height_vectorized(v0, theta, x)
        for yi, yi_expected in zip(y, y_expected):
            self.assertAlmostEqual(yi, yi_expected, delta=1e-3)        

if __name__ == "__main__":
    unittest.main()