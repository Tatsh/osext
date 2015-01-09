from os import chmod, mkdir, rmdir
import argparse
import unittest

from osext.argparse_actions import *

class TestArgparseActions(unittest.TestCase):
    _testdirs = []

    def test_readable_success(self):
        read = ReadableDirectoryAction(['-d'], 'r')
        try:
            mkdir('./read')
        except OSError:
            pass
        self._testdirs.append('./read')

        ns = argparse.Namespace()
        read(None, ns, './read')

        self.assertIn('/read', ns.r)

    def test_readable_failure(self):
        read = ReadableDirectoryAction(['-d'], 'r')
        try:
            mkdir('./read')
        except OSError:
            pass
        self._testdirs.append('./read')
        chmod('./read', 0)

        ns = argparse.Namespace()

        with self.assertRaises(argparse.ArgumentTypeError):
            read(None, ns, './read')

        chmod('./read', 425)

    def test_writable_success(self):
        write = WritableDirectoryAction(['-d'], 'w')
        try:
            mkdir('./write')
        except OSError:
            pass
        self._testdirs.append('./write')

        ns = argparse.Namespace()
        write(None, ns, './write')

        self.assertIn('/write', ns.w)

    def test_writable_failure(self):
        write = WritableDirectoryAction(['-d'], 'w')
        try:
            mkdir('./write')
        except OSError:
            pass
        chmod('./write', 292)
        self._testdirs.append('./write')

        ns = argparse.Namespace()
        with self.assertRaises(argparse.ArgumentTypeError):
            write(None, ns, './write')

    def tearDown(self):
        for dir in self._testdirs:
            try:
                rmdir(dir)
            except OSError:
                pass
