""" Functions test file
"""

import unittest
import advcubit.utility as _utility


class FunctionTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()


def testSuite():
    functionSuite = unittest.TestSuite()
    return functionSuite