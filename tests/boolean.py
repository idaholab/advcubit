""" Boolean test file
"""

import unittest

import advcubit.utility_module as _utility
import advcubit.boolean_module as _boolean
import advcubit.system_module as _system


class BooleanTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        pass

    def test_subtract(self):
        v1 = _system.cubitWrapper.brick(1, 1, 1)
        v2 = _system.cubitWrapper.brick(0.5, 0.5, 0.5)

        try:
            _boolean.subtract(v2, v1)
        except _system.AdvCubitException:
            self.assertTrue(False, 'Subtraction failed')


def testSuite():
    booleanSuite = unittest.TestSuite()
    booleanSuite.addTest(BooleanTest('test_subtract'))
    return booleanSuite
