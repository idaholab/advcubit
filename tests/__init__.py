import unittest

# import tests
import tests.system as system
import tests.utility as utility
import tests.wrapper as wrapper
import tests.functions as functions
import tests.transform as transform
import tests.boolean as boolean
import tests.vertex as vertex
import tests.curve as curve
import tests.surface as surface
import tests.volume as volume
import tests.imprint as imprint
import tests.mesh as mesh
import tests.sideset as sideset
import tests.block as block


def testSuite():
    advcubitTests = unittest.TestSuite()
    advcubitTests.addTest(system.testSuite())
    advcubitTests.addTest(utility.testSuite())
    advcubitTests.addTest(wrapper.testSuite())
    advcubitTests.addTest(functions.testSuite())
    advcubitTests.addTest(transform.testSuite())
    advcubitTests.addTest(boolean.testSuite())
    advcubitTests.addTest(vertex.testSuite())
    advcubitTests.addTest(curve.testSuite())
    advcubitTests.addTest(surface.testSuite())
    advcubitTests.addTest(volume.testSuite())
    advcubitTests.addTest(imprint.testSuite())
    advcubitTests.addTest(mesh.testSuite())
    advcubitTests.addTest(sideset.testSuite())
    advcubitTests.addTest(block.testSuite())
    return advcubitTests
