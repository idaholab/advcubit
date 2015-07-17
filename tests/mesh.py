""" Mesh test file
"""

import unittest
import advcubit.system_module as _system
import advcubit.utility_module as _utility
import advcubit.mesh_module as _mesh


class MeshTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()
        _utility.newFile()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()

    def test_quality(self):
        v = _system.cubitModule.brick(1, 1, 1)
        print(_mesh)
        _mesh.mesh(v)
        _mesh.meshQuality(v)


def testSuite():
    meshSuite = unittest.TestSuite()
    meshSuite.addTest(MeshTest('test_quality'))
    return meshSuite