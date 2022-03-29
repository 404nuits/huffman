#################################################
# Utils functions for Huffman coding / decoding #
#################################################

from collections import Counter
from heapq import heapify, heappop, heappush

class Node:
    def __init__(self, frequency, char=None, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left == None and self.right == None
    
    def is_empty(self):
        return self == None
    
    def __lt__(self, other):
        """Overwrite comparison function to tell to heapq what to compare in Node object

        Args:
            other (Node): Other node to compare with the current one

        Returns:
            bool: True if current lower than other, False else
        """
        return self.frequency < other.frequency
    
    def __gt__(self, other):
        return self.frequency > other.frequency
    
    def __str__(self):
        return '<'+ str(self.char)+'.'+str(self.left)+'.'+str(self.right)+'>'


# =============== Huffman functions ===============

def count(string):
    counter = Counter(string)
    return dict(counter)

def get_queue(frequences):
    queue = []
    for char in frequences:
        node = Node(frequences[char], char)
        queue.append(node)

    heapify(queue)

    return queue

def huffman(queue):
    while len(queue) > 1:

        # Get 2 lowest elements
        l1 = heappop(queue)
        l2 = heappop(queue)

        # Create new leaf node
        n = Node(l1.frequence + l2.frequence)
        n.left = l1
        n.right = l2
        
        # Add it to queue
        heappush(queue, n)

    return queue


# =============== Encoding / Decoding ===============

def encode(table, string):
    
    binary = ""

    for c in string:
        if not c in table:
            raise ValueError("TO CHANGE")
        binary += table[c]
    
    return binary


def decode(tree, bin_string):

    node = tree

    plain_text = ''

    for bit in bin_string:

        if bit == '0':
            node = node.left
        elif bit == '1':
            node = node.right
        else:
            raise ValueError("Not binary string")
        
        if node.is_leaf():
            plain_text += node.char

            # End of path, return to root
            node = tree
    
    return plain_text


# =============== File / Binary ===============

def write_bits_to_file(file, bin_string):
    """Transform a binary string into a bytearray and write it to a file

    Args:
        file (str): Path and name of file to write to
        bin_string (str): String composed only of 1 and 0s
    """

    i = 0

    buffer = bytearray()

    # Add byte per byte to buffer
    while i < len(bin_string):
        buffer.append(int(bin_string[i:i+8], 2))
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

    return bin_string


# =============== Functions for testing ===============

def is_compressed_smaller(string):
    pass

# =============== String / Binary ===============

def string_bin_to_16_bits(string, padding="0"):
    while len(string) < 16:
        string = padding + string
    return string

def string_to_binary(string):

    byte_list = []

    for c in bytearray(string, "utf8"):
        byte_list.append(bin(c)[2:])

    return "".join(byte_list)

def char_to_code_16_bits(char, padding="0"):
    code = '0' + bin(ord(char))[2:]

    while len(code) < 16:
        code = padding + code
    return code

def code_to_char_16_bits(code):
    """
    Convert a code to its char
    """
    return chr(int(code,2))