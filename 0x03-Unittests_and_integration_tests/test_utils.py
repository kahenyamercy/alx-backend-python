#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """TestAcessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_error_message):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_error_message)
