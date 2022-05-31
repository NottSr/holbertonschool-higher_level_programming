#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class that tests max_integer function
    """
    def test_max_integer(self):
        """
        Module that tests with proper values as args
        """
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-10, -5, -3, -1, 0]), 0)
        self.assertAlmostEqual(max_integer([1.5, 1.2, 2.3, 4.0]), 4.0)
        self.assertAlmostEqual(max_integer([10]), 10)

    def test_len(self):
        """
        Module that tests when there's no args in function
        """
        self.assertIsNone(max_integer([]))

    def test_errors(self):
        """
        Module that tests for errors
        """
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Hello", 24, "I'm", 12, "a", 53, "string"])
