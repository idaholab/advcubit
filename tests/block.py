""" block module testing
"""

import unittest


import advcubit.system as _system
import advcubit.utility as _utility
import advcubit.block as _block


testFolder = 'tests/'


class BlockTest(unittest.TestCase):

    def setUp(self):
        """ test set up function """
        _utility.startCubit()
        _utility.newFile()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()

    def test_create_block(self):
        v = _system.cubitModule.brick(1, 1, 1)
        try:
            _block.createBlock(v, 1, 'volume')
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))

    def test_element_type(self):
        v = _system.cubitModule.brick(1, 1, 1)
        _block.createBlock(v, 1, 'volume')
        try:
            _block.setBlockType(1, _block.VolumeElementTypes.HEX8)
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))

    def test_name_block(self):
        v = _system.cubitModule.brick(1, 1, 1)
        _block.createBlock(v, 1, 'volume')
        try:
            _block.nameBlock(1, 'testName')
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))


def testSuite():
    blockSuite = unittest.TestSuite()
    blockSuite.addTest(BlockTest('test_create_block'))
    blockSuite.addTest(BlockTest('test_element_type'))
    blockSuite.addTest(BlockTest('test_name_block'))
    return blockSuite