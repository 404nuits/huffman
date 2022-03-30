import huffman, huffman_nofreq

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

    files = [
        'bigFile',
        'littleFile',
        'leHorla'
    ]

    print("Freq")
    test_huffman_freq_all(files)
    print("No freq")
    test_huffman_no_freq_all(files)
