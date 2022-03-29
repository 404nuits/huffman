#####################################################
######  Introduction à la cryptographie  	      ###
#####   Codes de Huffman             		      ###
#####################################################

from heapq import *
from huffman_utils import *

###  distribution de proba sur les letrres

caracteres = [
    ' ', 'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z' ]

proba = [
    0.1835, 0.0640, 0.0064, 0.0259, 0.0260, 0.1486, 0.0078,
    0.0083, 0.0061, 0.0591, 0.0023, 0.0001, 0.0465, 0.0245,
    0.0623, 0.0459, 0.0256, 0.0081, 0.0555, 0.0697, 0.0572,
    0.0506, 0.0100, 0.0000, 0.0031, 0.0021, 0.0008  ]

def frequences() :
    table = {}
    n = len(caracteres)
    for i in range(n) :
        table[caracteres[i]] = proba[i]
    return table

F = frequences()


###  Ex.1  construction de l'arbre d'Huffman utilisant la structure de "tas binaire"
def arbre_huffman(frequences):
    """Generate huffman tree with a Node for NYT chars

    Args:
        frequences (dict): Frequencies dictionary (char -> frequency couples)

    Returns:
        Arbre: Huffman tree
    """

    # Add NYT to frequences with 0
    frequences['NYT'] = 0

    queue = get_queue(frequences)

    tree = huffman_tree(queue)

    # Return tree
    return tree


###  Ex.2  construction du code d'Huffamn
# Cf. huffman_utils.huffman_code

###  Ex.3  encodage d'un texte contenu dans un fichier
def encode(dico,file) :
    """Encode file using huffman dict, hadling NYT chars

    Args:
        dico (dict): Huffman dict (char -> path code couples)
        file (str): Filename

    Returns:
        str: Binary string of encoded data
    """

    encoded = ''

    # Read data from input file
    with open(file,'r', encoding="utf-8") as file:

        texte = file.read()

        # Replace each char by its path code 
        for char in texte:

            if char in dico:
                encoded += dico[char]

            else:
                # If the char is NYT, replace by path to NYT Node, then by its charcode on 16 bits
                encoded += dico['NYT'] + char_to_code_16_bits(char)

    return encoded

def encode_to_file(dico, file):
    """Encode data from file to binary file using huffman

    Args:
        dico (dict): Huffman dict (char -> path code couples)
        file (str): Input filename with data to encode
    """

    bin_string = encode(dico, file)

    # New filename = old filename basename + Encoded.bin
    file_encoded = file.rsplit('.',1)[0] + "Encoded.bin"

    write_bits_to_file(file_encoded, bin_string)

###  Ex.4  décodage d'un fichier compressé

def decode(tree, bin_file):
    """Decode a binary file encoded with huffman algorithm

    Args:
        tree (Arbre): Root of huffman tree
        bin_file (str): Input filename of binary data

    Returns:
        str: Decoded text
    """

    # Get bin string of encoded data
    bin_string = read_bits_from_file(bin_file)

    decoded = ''
    
    root = tree

    # Create an iterator to skip values whenever we want (useful for NYT handling)
    iter_string = iter(range(len(bin_string)))

    for i in iter_string:

        bit = bin_string[i]
        
        if bit == '1':
            tree = tree.droit
        
        elif bit == '0':
            tree = tree.gauche
        
        if arbre.estFeuille():
            
            if arbre.lettre == 'NYT':

                # If current char is NYT, that means that the next 16 bits are the charcode
                char_code = bin_string[i:i+17]

                # Decode char code
                char = code_to_char_16_bits(char_code)

                decoded += char

                # Skip next 16 bits
                [next(iter_string) for _ in range(16)]

            else:
                decoded += arbre.lettre

            arbre = root

    return decoded

def compress_to_file(tree, file):
    """Directly compress data from file to file using huffman algorithm

    Args:
        tree (Arbre): Huffman tree
        file (str): Input filename (containing clear data to encode)
    """

    code_huffman = huffman_code(tree)

    encode_to_file(code_huffman, file)


def decompress_from_file(tree, file):
    """Decompress huffman encoded data from binary file 

    Args:
        tree (Arbre): Huffman tree
        file (str): Filename of encoded data (binary file)

    Returns:
        str: Decoded data
    """
    return decode(tree, file)

if __name__ == "__main__":

    tree = arbre_huffman(F)

    compress_to_file(tree, 'leHorla.txt')

    decoded = decompress_from_file(tree, 'leHorlaEncoded.bin')

    print(decoded)
