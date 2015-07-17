""" Node and side sets test file
"""


import unittest
import advcubit.utility_module as _utility


class SetTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()


def testSuite():
    setSuite = unittest.TestSuite()
    return setSuite
