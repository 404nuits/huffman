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

def string_to_binary(string):

    byte_list = []

    for c in bytearray(string, "utf8"):
        byte_list.append(bin(c)[2:])

    return "".join(byte_list)


def encode(table, string):
    
    binary = ""

    for c in string:
        if not c in table:
            raise ValueError("TO CHANGE")
        binary += table[c]
    
    return binary


def decode(tree, bits_string):

    node = tree

    plain_text = ''

    for bit in bits_string:

        if bit == '0':
            node = node.left
        elif bit == '1':
            node = node.right
        else:
            raise ValueError("Not binary string")
        
        if node.char:
            plain_text += node.char

            # End of path, return to root
            node = tree
    
    return plain_text


# =============== Functions for testing ===============

def is_compressed_smaller(string):
    pass