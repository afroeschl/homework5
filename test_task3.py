""" Test for Task3: Checking the functionality in 'task3.py' using assertions """

import unittest
import os
import matplotlib.pyplot as plt
import task3


class Test(unittest.TestCase):
    def setUp(self):
        # (v0, theta) in (km/h, degrees)
        # Parameter set 1: fixed v0, varying theta
        self.lst_v0_theta_1 = [(72, 20), (72, 30), (72, 45), (72, 60), (72, 75)] # (v0, theta) in (km/h, degrees)
        self.lst_v0_theta_1.reverse()

        # Parameter set 2: varying v0, fixed theta
        self.lst_v0_theta_2 = [(36, 45), (54, 45), (72, 45), (90, 45), (108, 45)]
        self.lst_v0_theta_2.reverse()
        return super().setUp()
    
    def test_min_max_distance_1(self):
        # Parameter set 1: fixed v0, varying theta
        range_min, range_max = task3.min_max_distance(self.lst_v0_theta_1)
        
        # check returned values
        range_min_expected = 20.38735983690112 # m
        range_max_expected = 40.77471967380224 # m
        self.assertAlmostEqual(range_min, range_min_expected, delta=1e-2)
        self.assertAlmostEqual(range_max, range_max_expected, delta=1e-2)

    def test_min_max_distance_2(self):
        # Parameter set 2: varying v0, fixed theta
        range_min, range_max = task3.min_max_distance(self.lst_v0_theta_2)
        
        # check returned values
        range_min_expected = 10.19367991845056 # m
        range_max_expected = 91.74311926605505 # m
        self.assertAlmostEqual(range_min, range_min_expected, delta=1e-2)
        self.assertAlmostEqual(range_max, range_max_expected, delta=1e-2)

    def test_trajectories_1(self):
        # Parameter set 1: fixed v0, varying theta
        N = 50
        figname = "task3_N50.png"

        if os.path.isfile(figname): # if file pre-exists, remove it
            os.remove(figname)

        plt.close('all')
        task3.plot_trajectories(self.lst_v0_theta_1, figname, N)
        plt.close('all')

        # check plot fig created
        self.assertTrue(os.path.isfile(figname))

    def test_trajectories_2(self):
        # Parameter set 2: varying v0, fixed theta
        N = 10        
        figname = "task3_N10.png"
        
        if os.path.isfile(figname): # if file pre-exists, remove it
            os.remove(figname)

        plt.close('all')
        task3.plot_trajectories(self.lst_v0_theta_2, figname, N)
        plt.close('all')

        # check plot fig created
        self.assertTrue(os.path.isfile(figname))


if __name__ == "__main__":
    unittest.main()