################################################
## Implémentation de l'algorithme de Huffman  ##
####             Sans fréquence             ####
################################################

from heapq import heapify, heappop, heappush
from huffman_utils import *

def count(string):
    """generate a frequency dict for each char in the passed string

    Args:
        string (char): String to count frequency on

    Returns:
        dict: Dictionary with char as key and integer frequency as value
    """
    counts = {}
    for c in string:
        if c not in counts:
            counts[c]=0
        else:
            counts[c] += 1
    return counts

def encode(encoding, s):
    """Encode each char of string in parameter by its code indicated in the encoding variable

    Args:
        encoding (dict): dict associating each char with its code
        s (str): String to encode

    Raises:
        ValueError: Raises when a char in s is not present in the encoding dict

    Returns:
        str: String representation of encoded form of s, in binary
    """

    # Encoded form of s
    bits = ''

    for char in s:

        if not char in encoding:
            raise ValueError("'" + char + "' is not encoded character")

        bits += encoding[char]

    return bits

def decode(root, bin_string):
    """Decode a binary string and replace each code by a char based on the tree passed in parameters

    Args:
        root (Arbre): Huffman tree used to decode the binary string
        bin_string (str): String representation of binary data (only 0 and 1 accepted)

    Returns:
        str: Decoded form of data
    """
    node = root
    s = ''

    for bit in bin_string:

        if bit == '0':
            node = node.gauche

        else:
            node = node.droit

        if node.estFeuille():
            s += node.lettre
            node = root

    return s

def dict_to_binary(freq_dict):
    """Serialize a frequency dictionary to its binary representation

    The final string will contains, in order :
        - The length of the follow binary string (16 bits)
        - The serialized dict (in binary string)
            - Each char is encoded on 16 bits
            - Each frequency is encoded on 16 bits

        Each time, on those 16 bits, there is at least one padding bit, which is the opposite bit of the first bit of the encoded value
        For example, if a value has 0100 as its encoded form, padding will be made of ones, because the first bit is 0,
        So the final bit will be 1111111111110100.
    
    Args:
        dico (dict): Frequencies dictionary, it must only contains char -> frequency (int) couples.
        char being an UTF-8 character, and frequency an integer

    Returns:
        str: String representation of serialized frequency dictionary (in binary)
    """

    tree_string = ""

    # Dict to binary string
    for item in freq_dict.items():
        char = item[0]
        freq = item[1]

        # Encode char on 16 bits
        char_16b = char_to_code_16_bits(char)

        # Get frequency binary representation (removing the 'b' char coming with the bin() function)
        freq_16b = "0" + bin(freq)[2:]

        # Choosing padding based on first bit (padding is its opposite)
        padding = "0" if freq_16b[0]=="1" else "1"

        # Encode frequency on 16 bits, with opposite padding
        freq_16b = string_bin_to_16_bits(freq_16b,padding)

        tree_string += char_16b + freq_16b
    
    # Length
    length = len(tree_string)
    bin_length = string_bin_to_16_bits("0"+str(bin(length))[2:])

    return bin_length+tree_string

def decode_freq(string):
    """Decode binary representation of frequency dictionary

    Args:
        string (str): String representation of encoded binary data (must be only 0 and 1)
        It must contain the serialized dict, but also the encoded data

    Returns:
        dico: Deserialized frequencies dictionary
        string[length+16:]: Encoded binary data to decode (binary string)
    """

    # first 16 bits = length
    length = int(string[:16],2)

    # Get only tree values from length
    values = string[16:16+length]

    dico = {}

    # Looping through values, with a step of 32, so we'll have the encoded binary letter (first 16 bits), and its code (last 16 bits)
    for i in range(0,length,32):

        letter = values[i:i+16]
        code = values[i+16:i+32]

        # Decoding letter
        letter = code_to_char_16_bits(letter)

        # Retrieving padding bit
        padding = code[0]

        # Removing padding bits (which are the opposite of the first bit value)
        code = code.lstrip('1') if padding == "1" else code.lstrip('0')

        # Constructing the couple in the dict
        dico[letter] = int(code,2)

    return dico, string[length+16:]

def compress(s):
    """Compress a string to a binary string, using huffman algorithm

    Args:
        s (str): Clear string data

    Returns:
        str: Encoded version of the data, in binary string, with serialized frequencies heading
    """

    # Get frequencies of char in text
    frequencies = count(s)

    # Get priority queue
    queue = get_queue(frequencies)

    # Get huffman tree from queue
    root = huffman_tree(queue)

    # Get dict of char <-> code based on huffman tree
    tree_dict = huffman_code(root)

    # Encode clear string using dict    
    text_encoded = encode(tree_dict, s)

    # Get frequencies as binary string
    d_b = dict_to_binary(frequencies)

    # Concat the two bin strings to get everything we need to decode it later
    full_encoded = d_b + text_encoded

    return full_encoded

def compress_to_file(s,file):
    """Compress a string to a file using huffman algorithm

    Args:
        s (str): String to compress
        file (str): Filename to which compress the string
    """
    compressed = compress(s)

    # Write in byte mode to a binary file
    write_bits_to_file(file, compressed)

def decompress(s):
    """Retrieve a compressed data knowing only its compressed value

    Args:
        s (str): Binary string (must only contains 0 and 1) of compressed data, with heading serialized frequency dict (and its length at the very first)

    Returns:
        str: Decoded data
    """

    # Regenerate huffman tree from frequencies that are in the file
    # And then keep only encoded text to decode
    freq_dict,encoded_text = decode_freq(s)
    
    queue = get_queue(freq_dict)

    root = huffman_tree(queue)

    return decode(root,encoded_text)

def decompress_to_file(s,file):
    """Decompress compressed data to file, writing in UTF-8

    Args:
        s (str): Compressed data (binary string, with only 0 and 1)
        file (str): Output filename
    """
    decoded = decompress(s)
    with open(file, 'w', encoding="utf-8") as f:
        f.write(decoded)

if __name__ == '__main__':
    
    with open('leHorla.txt','r', encoding="utf-8") as f:
        clear = f.read()
    compressed = compress(clear)
    decompressed = decompress(compressed)

