""" Mesh test file
"""

import unittest
import advcubit.utility as _utility


class MeshTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()


def testSuite():
    meshSuite = unittest.TestSuite()
    return meshSuite