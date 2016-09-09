#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_dataset_generator
----------------------------------

Tests for `python_dataset_generator` module.
"""

import unittest
from unittest.mock import MagicMock, patch
from python_dataset_generator import python_dataset_generator


class TestPython_dataset_generator(unittest.TestCase):

    def setUp(self):
        self.generator = python_dataset_generator.python_dataset_generator()

    def test_default_instantiation(self):
        generator = python_dataset_generator.python_dataset_generator()
        self.assertIsInstance(generator, python_dataset_generator.python_dataset_generator)

    def test_saving_out_to_file(self):
        mock = MagicMock()

        open_name = '%s.open' % __name__
        with patch(open_name, mock, create=True):
            with open(self.generator._filename, 'w') as f:
                f.write('')

        self.generator.save()
        mock.assert_called_once_with(self.generator._filename, 'w')

    def tearDown(self):
        pass

