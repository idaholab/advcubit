""" Imprint test file
"""

import unittest
import advcubit.utility_module as _utility
import advcubit.system_module as _system
import advcubit.imprint_module as _imprint


class ImprintTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()

    def test_imprint(self):
        v1 = _system.cubitModule.brick(1, 1, 1)
        v2 = _system.cubitModule.brick(1, 1, 1)
        try:
            _imprint.imprint([v1, v2])
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))


def testSuite():
    imprintSuite = unittest.TestSuite()
    imprintSuite.addTest(ImprintTest('test_imprint'))
    return imprintSuite