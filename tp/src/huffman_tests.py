import unittest

class TestFileMethods(unittest.TestCase):


    def test_size(self):
        self.assertTrue(True)

    def test_content(self):
        self.assertEqual("a","a")

if __name__ == '__main__':
    unittest.main()