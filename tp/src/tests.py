#test.py
import unittest
import huffman_nofreq
import sys

class TestLengthFile(unittest.TestCase):
    
    def test_negativeForLess(self):
        size_compressed = 6
        size_initial = 5
        # error message in case if test case got failed
        message = "Le fichier compressé est plus grand que le fichier initial."
          
        # assert function() to check if values1 is less than value2
        self.assertLess(size_compressed, size_initial, message)

if __name__ == '__main__':
    unittest.huffman_nofreq.main()