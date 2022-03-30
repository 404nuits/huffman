import unittest
import huffman

class TestFileMethods(unittest.TestCase):
    

    def test_content_little_file(self):
        filename="littleFile.txt"
        filename_encoded="littleFileEncoded.bin"
        F=huffman.frequences()
        tree = huffman.arbre_huffman(F)

        decoded = huffman.decompress_from_file(tree, filename_encoded)

        with open(filename,'r', encoding="utf-8") as f:
            clear = f.read()
        self.assertEqual(clear,decoded)

    def test_content_big_file(self):
        filename="bigFile.txt"
        filename_encoded="bigFileEncoded.bin"
        F=huffman.frequences()
        tree = huffman.arbre_huffman(F)

        decoded = huffman.decompress_from_file(tree, filename_encoded)

        with open(filename,'r', encoding="utf-8") as f:
            clear = f.read()
        self.assertEqual(hash(clear),hash(decoded))

    def test_content_leHorla(self):
        filename="leHorla.txt"
        filename_encoded="leHorlaEncoded.bin"
        F=huffman.frequences()
        tree = huffman.arbre_huffman(F)

        decoded = huffman.decompress_from_file(tree, filename_encoded)
        
        with open(filename,'r', encoding="utf-8") as f:
            clear = f.read()
        self.assertEqual(clear,decoded)

if __name__ == '__main__':
    unittest.main()