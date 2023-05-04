import unittest

class TestApp(unittest.TestCase):
    
    def test_assert_true(self):
        self.assertTrue(True)

    def test_assert_false(self):
        self.assertTrue(False)

    def test_assert_equals(self):
        self.assertEqual("","1")