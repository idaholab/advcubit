import unittest

# import tests
import tests.system as system
import tests.utility as utility
import tests.block as block

def testSuite():
    advcubitTests = unittest.TestSuite()
    advcubitTests.addTest(system.testSuite())
    advcubitTests.addTest(utility.testSuite())
    advcubitTests.addTest(block.testSuite())
    return advcubitTests
