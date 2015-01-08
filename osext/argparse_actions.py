# coding: utf-8

from os.path import isdir
import argparse
import os


class ReadableDirectoryAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir = values

        if not isdir(prospective_dir):
            raise argparse.ArgumentTypeError('%s is not a valid directory' % (
                prospective_dir,
            ))

        if os.access(prospective_dir, os.R_OK):
            setattr(namespace, self.dest, realpath(prospective_dir))
            return

        raise argparse.ArgumentTypeError('%s is not a readable directory' % (
            prospective_dir,
        ))


class WritableDirectoryAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir = values

        if not isdir(prospective_dir):
            raise argparse.ArgumentTypeError('%s is not a valid directory' % (
                prospective_dir,
            ))

        if os.access(prospective_dir, os.W_OK):
            setattr(namespace, self.dest, realpath(prospective_dir))
            return

        raise argparse.ArgumentTypeError('%s is not a readable directory' % (
            prospective_dir,
        ))
