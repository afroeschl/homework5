""" Test for Task1: Checking the functionality in 'task1.py' using assertions """

import unittest
import io
import sys
import os
import runpy
import matplotlib.pyplot as plt


class Test(unittest.TestCase):
    def test_task1(self):

        figname = "task1.png"
        if os.path.isfile(figname): # if file pre-exists, remove it
            os.remove(figname)

        plt.close('all')
        
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput         #  and redirect stdout.
        runpy.run_path("task1.py", run_name="__main__") # run task1
        sys.stdout = sys.__stdout__         # Reset redirect.
        # content = capturedOutput.getvalue() # get console output
        
        plt.close('all')
        self.assertTrue(os.path.isfile(figname))
        plt.close('all')

if __name__ == "__main__":
    unittest.main()
