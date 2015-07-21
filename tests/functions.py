""" Functions test file
"""

import unittest
import advcubit.utility_module as _utility
import advcubit.function_module as _functions
import advcubit.common_module as _common
import advcubit.system_module as _system


class FunctionTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()
        _utility.newFile()

    def tearDown(self):
        """ test shutdown function """
        # _utility.closeCubit()

    def test_body_type(self):
        v = _system.cubitModule.brick(1, 1, 1)
        self.assertEqual(_functions.getBodyType(v), _common.BodyTypes.body,
                         'Body detection failed')
        self.assertEqual(_functions.getBodyType(v.volumes()[0]), _common.BodyTypes.volume,
                         'Volume detection failed')
        self.assertEqual(_functions.getBodyType(v.surfaces()[0]), _common.BodyTypes.surface,
                         'Surface detection failed')
        self.assertEqual(_functions.getBodyType(v.curves()[0]), _common.BodyTypes.curve,
                         'Curve detection failed')
        self.assertEqual(_functions.getBodyType(v.vertices()[0]), _common.BodyTypes.vertex,
                         'Vertex detection failed')
        self.assertRaises(_system.AdvCubitException, _functions.getBodyType, '')

    def test_list_id_str(self):
        v = _system.cubitModule.brick(1, 1, 1)
        self.assertEqual(_functions.listIdString(v), (_common.BodyTypes.body, ' 1'))
        self.assertEqual(_functions.listIdString(v.bodies()), (_common.BodyTypes.body, ' 1'))
        self.assertEqual(_functions.listIdString(v.volumes()), (_common.BodyTypes.volume, ' 1'))
        self.assertEqual(_functions.listIdString(v.surfaces()), (_common.BodyTypes.surface, ' 1 2 3 4 5 6'))
        self.assertEqual(_functions.listIdString(v.curves()), (_common.BodyTypes.curve, ' 1 2 3 4 5 6 7 8 9 10 11 12'))
        self.assertEqual(_functions.listIdString(v.vertices()), (_common.BodyTypes.vertex, ' 1 2 3 4 5 6 7 8'))


def testSuite():
    functionSuite = unittest.TestSuite()
    functionSuite.addTest(FunctionTest('test_body_type'))
    functionSuite.addTest(FunctionTest('test_list_id_str'))
    return functionSuite