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
        v = _system.cubitWrapper.brick(1, 1, 1)
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
        v = _system.cubitWrapper.brick(1, 1, 1)
        self.assertEqual(_functions.listIdString(v), (_common.BodyTypes.body, ' 1'))
        self.assertEqual(_functions.listIdString(v.bodies()), (_common.BodyTypes.body, ' 1'))
        self.assertEqual(_functions.listIdString(v.volumes()), (_common.BodyTypes.volume, ' 1'))
        self.assertEqual(_functions.listIdString(v.surfaces()), (_common.BodyTypes.surface, ' 1 2 3 4 5 6'))
        self.assertEqual(_functions.listIdString(v.curves()), (_common.BodyTypes.curve, ' 1 2 3 4 5 6 7 8 9 10 11 12'))
        self.assertEqual(_functions.listIdString(v.vertices()), (_common.BodyTypes.vertex, ' 1 2 3 4 5 6 7 8'))

    def test_interval(self):
        v1 = _system.cubitWrapper.brick(1, 1, 1)
        v2 = _system.cubitWrapper.brick(1, 1, 1)
        v3 = _system.cubitWrapper.brick(1, 1, 1)
        v4 = _system.cubitWrapper.brick(1, 1, 1)
        _system.cubitModule.move(v2, [1.0, 0, 0])
        _system.cubitModule.move(v3, [1.1, 0, 0])
        _system.cubitModule.move(v4, [0, 1.0, 0])

        self.assertEqual(_functions.searchOverlaps([v1, v2, v3, v4]).sort(),
                         [(v1, v2), (v2, v3), (v1, v4), (v2, v4)].sort(),
                         'Pair detection failed')

    def test_get_entities(self):
        v1 = _system.cubitWrapper.brick(1, 1, 1)
        self.assertEqual(_functions.getEntities(_common.BodyTypes.body, 'all').sort(), [v1.bodies()].sort(),
                         'Body finding failed')
        self.assertEqual(_functions.getEntities(_common.BodyTypes.volume, 'all').sort(), [v1.volumes()].sort(),
                         'Volume finding failed')
        self.assertEqual(_functions.getEntities(_common.BodyTypes.surface, 'all').sort(), [v1.surfaces()].sort(),
                         'Surface finding failed')
        self.assertEqual(_functions.getEntities(_common.BodyTypes.curve, 'all').sort(), [v1.curves()].sort(),
                         'Curve finding failed')
        self.assertEqual(_functions.getEntities(_common.BodyTypes.vertex, 'all').sort(), [v1.vertices()].sort(),
                         'Vertex finding failed')


def testSuite():
    functionSuite = unittest.TestSuite()
    functionSuite.addTest(FunctionTest('test_body_type'))
    functionSuite.addTest(FunctionTest('test_list_id_str'))
    functionSuite.addTest(FunctionTest('test_interval'))
    functionSuite.addTest(FunctionTest('test_get_entities'))
    return functionSuite
