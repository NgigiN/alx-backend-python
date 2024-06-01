#!/usr/bin/env python3
"""This module tests the functions present in utils.py"""
import requests
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class with the tests for utils.access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """The test itself for the function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests if the a KeyError is raised"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class with the tests for utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests the method returns the expected result"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Class to test the memoize decorator"""

    class TestClass:
        """Class with methods to test memoization"""

        def a_method(self):
            """method for testing"""
            return 42

        @memoize
        def a_property(self):
            """A property memoized using the memoize decorator"""
            return self.a_method()

    def test_memoize(self):
        """Tests for the memoize decorator"""

        test_obj = self.TestClass()

        with patch.object(test_obj, 'a_method') as mock_a_method:
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(result1, result2)
