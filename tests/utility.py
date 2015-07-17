""" Test module of advcubit utility functions """

import unittest
import tests.settings as _settings

import advcubit.system_module as _system
import advcubit.utility_module as _utility


class UtilityTest(unittest.TestCase):
    def setUp(self):
        """ test set up function """
        _utility.startCubit()

    def tearDown(self):
        """ test shutdown function """
        _utility.closeCubit()

    def test_new_file(self):
        try:
            _utility.newFile()
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))

    def test_open_file(self):
        try:
            _utility.open(_settings.testFolder + 'test.cub')
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))

    def test_save_file(self):
        try:
            _utility.save(_settings.testFolder + 'test2.cub')
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))

    def test_export(self):
        _utility.open(_settings.testFolder + 'test.cub')
        try:
            _utility.export(_settings.testFolder + 'test.e')
        except _system.AdvCubitException as e:
            self.assertTrue(False, str(e))


def testSuite():
    utilitySuite = unittest.TestSuite()
    utilitySuite.addTest(UtilityTest('test_new_file'))
    utilitySuite.addTest(UtilityTest('test_open_file'))
    utilitySuite.addTest(UtilityTest('test_save_file'))
    utilitySuite.addTest(UtilityTest('test_export'))
    return utilitySuite
