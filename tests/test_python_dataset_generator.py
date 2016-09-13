#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_dataset_generator
----------------------------------

Tests for `python_dataset_generator` module.
"""

import unittest
from unittest.mock import MagicMock, patch
from python_dataset_generator.python_dataset_generator import PythonDataSetGenerator


class TestPython_dataset_generator(unittest.TestCase):

    def setUp(self):
        self.generator = PythonDataSetGenerator()

    def test_default_instantiation(self):
        self.assertIsInstance(self.generator, PythonDataSetGenerator)

    def test_saving_out_to_file(self):
        mock = MagicMock()

        open_name = '%s.open' % __name__
        with patch(open_name, mock, create=True):
            with open(self.generator._filename, 'w') as f:
                f.write('')

        self.generator.save()
        mock.assert_called_once_with(self.generator._filename, 'w')

    def test_add_a_factor(self):
        self.generator.add_factor('factor_name', [34, 33], [344, 343])

    def test_add_a_factor_int_only(self):
        self.generator.add_factor('factor_name', 0, 10)


    def tearDown(self):
        pass

