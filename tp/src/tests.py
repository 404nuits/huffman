#test.py
import huffman_nofreq
import huffman
import os


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
    print("Le taux de compression est de :",compression_rate,'%')
    print("\n")

#
#
#   TESTS ABOUT THE CONTENT OF THE FILES
# 
#  



def check_diff(clear_in, clear_out, basename=""):

    print('--------')
    if clear_in == clear_out:
        print(basename+' : OK')
    else:
        print(basename+' : KO')
        print(f"Diff : ")
        print(f"In :    [Début]{clear_in[-20:]}[Fin]")
        print(f"Out :   [Début]{clear_out[-20:]}[Fin]")
    print('--------')
    print(' ')

def test_huffman_freq_all(files):

    tree = huffman.arbre_huffman(huffman.F)

    for f in files:
        test_huffman_freq(f,tree)


def test_huffman_freq(basename, tree):

    with open(basename+'.txt','r',encoding="utf-8") as f:
        clear_in = f.read()

    huffman.compress_to_file(tree, basename+'.txt')

    clear_out = huffman.decompress_from_file(tree, basename+'Encoded.bin')

    check_diff(clear_in,clear_out,basename)


def test_huffman_no_freq(basename):

    with open(basename+'.txt','r',encoding="utf-8") as f:
        clear_in = f.read()

    huffman_nofreq.compress_to_file(clear_in, basename+'EncodedNoFreq.bin')

    clear_out = huffman_nofreq.decompress_from_file(basename+'EncodedNoFreq.bin')

    check_diff(clear_in,clear_out, basename)

def test_huffman_no_freq_all(files):
    for f in files:
        test_huffman_no_freq(f)




if __name__ == '__main__':

    # name of files to test (without extension, they must be .txt)
    files = [
        '../data/bigFile',
        '../data/littleFile',
        '../data/leHorla'
    ]
    

    # ========= Size Comparison =========

    # ----- Huffman No Frequency -----

    # TESTS to compare size files with huffman_nofreq.py
    for file in files:
        createFileEncoded_nofreq(file+".txt",file+"EncodedNoFreq.bin")


    print("Comparaison des tailles de fichiers avec l'utilisation de l'algorithme d'huffman sans fréquence :")
    for file in files:
        compareSize(file+".txt",file+"EncodedNoFreq.bin")


    # ----- Huffman with frequencies -----

    # TESTS to compare size files with huffman.py
    for file in files:
        createFileEncoded(file+".txt")
    
    print("Comparaison des tailles de fichiers avec l'utilisation de l'algorithme d'huffman avec fréquence :")
    for file in files:
        compareSize(file+".txt",file+"Encoded.bin")


    # ========= Content Comparison =========

    # TESTS to compare the content of files

    print("Vérification de l'équivalence entre le contenu du fichier initial et le contenu décodé du fichier encodé avec l'algorithme d'huffman")
    test_huffman_freq_all(files)
    print("Vérification de l'équivalence entre le contenu du fichier initial et le contenu décodé du fichier encodé avec l'algorithme d'huffman sans fréquence")
    test_huffman_no_freq_all(files)