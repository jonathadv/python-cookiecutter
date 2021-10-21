# pylint: disable=no-self-use

import unittest

from {{cookiecutter.project_slug}}.core import main


class TestMain(unittest.TestCase):
    """Core module Test Case"""

    def test_main_function(self):
        """The main function should return True"""
        assert main()
