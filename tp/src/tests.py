#test.py
import huffman_nofreq
import huffman
import os
import huffman_tests

def createFileEncoded_nofreq(filename,filename_encoded):
    
    with open(filename,'r', encoding="utf-8") as f:
        clear = f.read()

    #Compression du fichier
    huffman_nofreq.compress_to_file(clear,filename_encoded)

def createFileEncoded(filename):
    F=huffman.frequences()
    tree = huffman.arbre_huffman(F)

    huffman.compress_to_file(tree, filename)

    


def compareSize(filename,filename_encoded):
    size_compressed = os.path.getsize(filename_encoded)
    size_initial = os.path.getsize(filename)
    compression_rate = int(((size_initial-size_compressed)/size_initial)*100)
    print("Le fichier initial (",filename,") a une taille de : ",size_initial,"octets")
    print("Le fichier compressé a une taille de : ",size_compressed,"octets")
    print("Le taux de compression est de :",compression_rate)
    print("\n")
    

if __name__ == '__main__':

    createFileEncoded_nofreq("littleFile.txt","littleFileEncodedNofreq.bin")
    createFileEncoded_nofreq("bigFile.txt","bigFileEncodedNoFreq.bin")
    createFileEncoded_nofreq("leHorla.txt","leHorlaEncodedNoFreq.bin")

    print("Comparaison des tailles de fichiers avec l'utilisation de l'algorithme d'huffman sans fréquence :")
    compareSize("littleFile.txt","littleFileEncodedNoFreq.bin")
    compareSize("bigFile.txt","bigFileEncodedNoFreq.bin")
    compareSize("leHorla.txt","leHorlaEncodedNoFreq.bin")


    createFileEncoded("littleFile.txt")
    createFileEncoded("bigFile.txt")
    createFileEncoded("leHorla.txt")
    
    print("Comparaison des tailles de fichiers avec l'utilisation de l'algorithme d'huffman avec fréquence :")
    compareSize("littleFile.txt","littleFileEncoded.bin")
    compareSize("bigFile.txt","bigFileEncoded.bin")
    compareSize("leHorla.txt","leHorlaEncoded.bin")

    #huffman_tests.unittest.main()

    

