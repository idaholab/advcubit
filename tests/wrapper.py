""" Wrapper test file
"""

import unittest

import advcubit as _module
import advcubit.utility_module as _utility
import advcubit.wrapper_module as _wrapper


class WrapperTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        # _utility.closeCubit()

    def test_avail(self):
        self.assertTrue('get_default_element_type' in vars(_wrapper),
                        'Function not found in wrapper')
        self.assertTrue('get_default_element_type' in vars(_module),
                        'Function not found in advcubit')

    def test_fct_call(self):
        self.assertEqual(_wrapper.get_default_element_type(), 'hex',
                         'Test function not executed')


def testSuite():
    wrapperSuite = unittest.TestSuite()
    wrapperSuite.addTest(WrapperTest('test_avail'))
    wrapperSuite.addTest(WrapperTest('test_fct_call'))
    return wrapperSuite
