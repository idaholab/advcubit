""" Volume test file
"""

import unittest
import advcubit.utility_module as _utility


class VolumeTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()


def testSuite():
    volumeSuite = unittest.TestSuite()
    return volumeSuite