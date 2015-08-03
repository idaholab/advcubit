""" Transform test file
"""

import unittest

import advcubit.system_module as _system
import advcubit.transform_module as _transform
import advcubit.utility_module as _utility


class TransformTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        pass

    def test_move(self):
        v1 = _system.cubitWrapper.brick(1, 1, 1)

        try:
            _transform.move(v1, (1, 1, 1))
        except _system.AdvCubitException:
            self.assertTrue(False, 'Move failed')


def testSuite():
    transformSuite = unittest.TestSuite()
    transformSuite.addTest(TransformTest('test_move'))
    return transformSuite