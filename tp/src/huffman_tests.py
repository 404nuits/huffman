import unittest
import huffman
import huffman_nofreq

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


    def test_content_little_file_no_freq(self):
        filename="littleFile.txt"
        filename_encoded="littleFileEncodedNoFreq.bin"
       
        with open(filename_encoded,'r') as f:
            encoded = f.read()

        decoded = huffman_nofreq.decompress(encoded)

        with open(filename,'r', encoding="utf-8") as f:
            clear = f.read()
        self.assertEqual(clear,decoded)

    def test_content_big_file_no_freq(self):
        filename="bigFile.txt"
        filename_encoded="bigFileEncodedNoFreq.bin"
        
        with open(filename_encoded,'rb') as f:
            encoded = f.read()

        decoded = huffman_nofreq.decompress(encoded)

        with open(filename,'r', encoding="utf-8") as f:
            clear = f.read()
        self.assertEqual(hash(clear),hash(decoded))

    def test_content_leHorla_no_freq(self):
        filename="leHorla.txt"
        filename_encoded="leHorlaEncodedNoFreq.bin"
        
        with open(filename_encoded,'rb') as f:
            encoded = f.read()

        decoded = huffman_nofreq.decompress(encoded)
        
        with open(filename,'r', encoding="utf-8") as f:
            clear = f.read()
        self.assertEqual(clear,decoded)

if __name__ == '__main__':
    unittest.main()