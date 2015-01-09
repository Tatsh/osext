from osext.test import argparse_actions_test, pushdtest
import unittest

for test in (pushdtest, argparse_actions_test):
    suite = unittest.TestLoader().loadTestsFromModule(test)
    unittest.TextTestRunner(verbosity=2).run(suite)
