#!/bin/python

import unittest
import sys
import advcubit

# import test suits
import tests

print('Running advcubit test suite:')

try:
    advcubit.init(silentMode=False)
except EnvironmentError as e:
    print('Error initializing advcubit. $PYTHON_PATH must be set!\n' + str(e))
    sys.exit(1)

# run tests
testSuite = tests.testSuite()
try:
    unittest.main(defaultTest='testSuite')
finally:
    # clean journal files
    advcubit.deleteJournalFiles()
