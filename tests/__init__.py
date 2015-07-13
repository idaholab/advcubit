import unittest

# import tests
import tests.utility as utility
import tests.system as system

def testSuite():
    advcubitTests = unittest.TestSuite()
    advcubitTests.addTest(system.testSuite())
    advcubitTests.addTest(utility.testSuite())
    return advcubitTests
