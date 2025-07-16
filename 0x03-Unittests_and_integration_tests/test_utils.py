#!/usr/bin/env python3
"""Unit tests for utils.memoize"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test class for utils.memoize"""

    def test_memoize(self):
        """Test that memoize caches method result"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_obj = TestClass()

            # First call - should invoke a_method
            result1 = test_obj.a_property
            # Second call - should use cached result
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
