""" Vertex test file
"""

import unittest
import advcubit.utility_module as _utility


class VertexTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()


def testSuite():
    vertexSuite = unittest.TestSuite()
    return vertexSuite