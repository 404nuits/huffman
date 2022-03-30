#################################################
# Utils functions for Huffman coding / decoding #
#################################################

from heapq import heapify, heappop, heappush

class Arbre:
    def __init__(self, lettre, frequence, gauche=None, droit=None):

        self.gauche=gauche
        self.droit=droit
        self.lettre=lettre
        self.frequence=frequence

    def estFeuille(self):

        return self.gauche == None and self.droit == None

    def estVide(self):

        return self == None

    def __str__(self):
        return '<'+ str(self.lettre)+'.'+str(self.gauche)+'.'+str(self.droit)+'>'

    def __gt__(self, other):
        return self.frequence > other.frequence

    def __lt__(self, other):
        return self.frequence < other.frequence


# =============== Huffman functions ===============

def get_queue(frequences):
    """Generate a heap queue of Nodes, with the sort based on the frequency (cf __gt__ and __lt__ functions of Arbre class)

    Args:
        frequences (dict): Frequency dictionary, with only couples char -> frequency

    Returns:
        list: Nodes heap
    """
    heap = []

    for char in frequences:

        node = Arbre(char, frequences[char])

        heap.append(node)

    heapify(heap)

    return heap

def huffman_tree(queue):
    """Generate huffman tree based on heap queue
    To sort the heap, heapq uses the __gt__ operator, defined in the Arbre class

    Args:
        queue (list): Heap queue of nodes

    Returns:
        Arbre: huffman tree
    """
    while len(queue) > 1:

        # Get 2 lowest elements
        tree1 = heappop(queue)
        tree2 = heappop(queue)

        # Create new node
        proba = tree1.frequence + tree2.frequence
        char = tree1.lettre + tree2.lettre
        node = Arbre(char, proba, tree1, tree2)

        # Add it to the queue
        heappush(queue, node)

    return queue[0]

def infix_traversal(tree, prefix, code):
    """Do an infix traversal of a huffman tree, and generate a dict of char -> binary code (str) couples 

    Args:
        tree (Arbre): Node of huffman tree
        prefix (str): Binary string representation of path of char (0 = left, 1 = right)
        code (dict): Dictionary of binary string path representation for each char
    """
    
    if (tree.estFeuille()):
        code[tree.lettre] = prefix
    else:
        if tree.gauche != None:
            infix_traversal(tree.gauche,prefix+'0',code)
        if tree.droit != None:
            infix_traversal(tree.droit,prefix+'1',code)

def huffman_code(tree):
    """Generate huffman dictionary (char -> code) using infix traversal

    Args:
        tree (Arbre): root node of tree

    Returns:
        dict: Huffman dictionary
    """
    code = {}
    infix_traversal(tree, '', code)
    return code

# =============== File / Binary ===============

def write_bits_to_file(file, bin_string):
    """Transform a binary string into a bytearray and write it to a file

    Args:
        file (str): Path and name of file to write to
        bin_string (str): String composed only of 1 and 0s
    """

    i = 0

    # Calculate how many bits will be added when writing to byte array, to remove them while decoding
    noise_bits = (8 - (len(bin_string) % 8)) % 8

    # Convert to binary and removing the "b" char
    noise_bits = "0" + bin(noise_bits)[2:]
    
    # Convert this number to 8 bits (to keep an entire bytearray so the noise_bits value is still true)
    noise_bits = string_bin_to_n_bits(noise_bits,8)

    bin_string = noise_bits + bin_string

    buffer = bytearray()

    # Add byte per byte to buffer
    while i < len(bin_string):

        byte = bin_string[i:i+8]

        # Add trailing padding to last byte if necessary
        while len(byte) < 8:
            byte += "0"

        byte = int(byte,2)

        buffer.append(byte)
        i += 8

    with open(file, 'bw') as f:
        f.write(buffer)

def read_bits_from_file(file):
    """Read binary file to a string of bytes

    Args:
        file (str): Filename

    Returns:
        str: String representation of binary file
    """

    bin_string = ""

    with open(file, 'rb') as f:
        bytes = f.read()

    for byte in bytes:
        byte = str(bin(byte)[2:])

        # Add padding bits if necessary
        while len(byte) < 8:
            byte = "0" + byte

        bin_string += byte

    # Compute noise bits
    noise_bits = int(bin_string[:8],2)

    # Remove noise bits and their length value from bin string
    bin_string = bin_string[8:-noise_bits] if noise_bits != 0 else bin_string[8:]
    return bin_string

# =============== String / Binary ===============

def string_bin_to_n_bits(string,n):
    """Transform a binary string to a n bits binary string, adding leading padding bits

    Args:
        string (str): Binary string (only 0 and 1) lower than n bits

    Returns:
        str: n bits string
    """
    while len(string) < n:
            string = "0" + string
    return string

def string_bin_to_16_bits(string):
    """Transform a binary string to a 16 bits binary string, adding leading padding bits

    Args:
        string (str): Binary string (only 0 and 1) lower than 16 bits

    Returns:
        str: 16 bits string
    """
    return string_bin_to_n_bits(string, 16)

def char_to_code_16_bits(char):
    """Convert an UTF-8 char to a 16 bits binary string, with leading padding

    Args:
        char (str): char from UTF-8 table

    Returns:
        str: 16 bits binary string
    """
    code = '0' + bin(ord(char))[2:]

    while len(code) < 16:
        code = "0" + code
    return code

def code_to_char_16_bits(code):
    """Convert a bin string char code to its char

    Args:
        code (str): Binary string (1 and 0)

    Returns:
        str: char from bin string char code
    """
    return chr(int(code,2))