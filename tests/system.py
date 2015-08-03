""" system test suite
"""

import unittest
import advcubit.system_module as _system
import advcubit.utility_module as _utility


class SystemTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()

    def test_exception(self):
        self.assertRaises(_system.AdvCubitException, _utility.open, 'no_file')


def testSuite():
    systemSuite = unittest.TestSuite()
    systemSuite.addTest(SystemTest('test_exception'))
    return systemSuite