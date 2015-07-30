""" Imprint test file
"""

import unittest

import advcubit.system_module as _system
import advcubit.utility_module as _utility
import advcubit.transform_module as _transform
import advcubit.imprint_module as _imprint


class ImprintTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        # _utility.closeCubit()

    def test_imprint(self):
        v1 = _system.cubitWrapper.brick(1, 1, 1)
        v2 = _system.cubitWrapper.brick(1, 1, 1)
        try:
            _imprint.imprint([v1, v2])
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))

    def test_merge(self):
        v1 = _system.cubitWrapper.brick(1, 1, 1)
        v2 = _system.cubitWrapper.brick(1, 1, 1)
        _imprint.imprint([v1, v2])
        try:
            _imprint.merge([v1, v2])
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))

    def test_smart_imprint(self):
        v1 = _system.cubitWrapper.brick(1, 1, 1)
        v2 = _system.cubitWrapper.brick(1, 1, 1)
        v3 = _system.cubitWrapper.brick(1, 1, 1)
        _transform.move(v2, [1.0, 0, 0])
        _transform.move(v3, [1.2, 0, 0])
        try:
            _imprint.smartImprint([v1, v2, v3])
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))

    def test_smart_merge(self):
        v1 = _system.cubitWrapper.brick(1, 1, 1)
        v2 = _system.cubitWrapper.brick(1, 1, 1)
        v3 = _system.cubitWrapper.brick(1, 1, 1)
        _transform.move(v2, [1.0, 0, 0])
        _transform.move(v3, [1.2, 0, 0])
        _imprint.smartImprint([v1, v2, v3])
        try:
            _imprint.smartMerge([v1, v2, v3])
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))


def testSuite():
    imprintSuite = unittest.TestSuite()
    imprintSuite.addTest(ImprintTest('test_imprint'))
    imprintSuite.addTest(ImprintTest('test_smart_imprint'))
    imprintSuite.addTest(ImprintTest('test_merge'))
    imprintSuite.addTest(ImprintTest('test_smart_merge'))
    return imprintSuite
