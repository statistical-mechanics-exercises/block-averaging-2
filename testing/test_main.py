import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_energies(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_y)==10, "Wrong number of energies in list for graph" )
        for i in range(10) :
            thisav = sum( eng[i*100:(i+1)*100] ) / 100 
            self.assertTrue( np.abs( thisav - this_y[i] )<1e-7, "Incorrect values for block averages" )
