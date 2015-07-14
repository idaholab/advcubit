""" Transform test file
"""

import unittest
import advcubit.utility as _utility


class TransformTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()


def testSuite():
    transformSuite = unittest.TestSuite()
    return transformSuite