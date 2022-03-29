#test.py
import unittest
import main
import sys
import os

class TestLengthFile(unittest.TestCase):
    
    def test_negativeForLess(self):
        path_encoded="leHorla.bin"
        path_initial="leHorla.txt"
        main.compress(path_initial,path_encoded)
        size_compressed = os.path.getsize(path_encoded)
        size_initial = os.path.getsize(path_initial)
        # error message in case if test case got failed
        message = "Le fichier compressé est plus grand que le fichier initial."
          
        # assert function() to check if values1 is less than value2
        self.assertLess(size_compressed, size_initial, message)

if __name__ == '__main__':
    unittest.main()