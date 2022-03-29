################################################
## Implémentation de l'algorithme de Huffman  ##
####             Sans fréquence             ####
################################################

from heapq import heapify, heappop, heappush
from huffman_utils import *

class Node:
    def __init__(self, frequence, char=None, left=None, right=None):
        self.char = char
        self.frequence = frequence
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left == None and self.right == None
        
    def isEmpty(self):
        return self == None

    def __lt__(self, other):
        return self.frequence < other.frequence

    def __gt__(self, other):
        return self.frequence > other.frequence

    def __str__(self):
        return '<'+ str(self.char)+'.'+str(self.left)+'.'+str(self.right)+'>'

    def encode(self, encoding):
        """Return bit encoding in traversal."""
        if self.left is None and self.right is None:
            yield (self.char, encoding)
        else:
            for v in self.left.encode(encoding + '0'):
                yield v
            for v in self.right.encode(encoding + '1'):
                yield v

# Frequency count
def count(string):
    counts = {}
    for c in string:
        if c not in counts:
            counts[c]=0
        else:
            counts[c] += 1
    return counts


# Construction of priority queue
def queue(frequences):
    queue = []
    for char in frequences:
        nono = Node(frequences[char], char)
        queue.append(nono)

    heapify(queue)

    return queue

# Duffman
def duffman(queue):
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


    return queue[0]


# Record
def record(queue):
    root = queue
    encoding = {}

    for sym, code in root.encode(''):
        encoding[sym]=code

    return encoding


def encode(encoding, s):
    """Return bit string for encoding."""
    bits = ''
    for _ in s:
        if not _ in encoding:
            raise ValueError("'" + _ + "' is not encoded character")
        bits += encoding[_]
    
    return bits


def decode(root, bits):
    """Decode ASCII bit string for simplicity."""
    node = root
    s = ''
    for _ in bits:
        if _ == '0':
            node = node.left
        else:
            node = node.right
        if node.char:
            s += node.char
            node = root
    return s

def parcours(arbre,prefixe,code) :

    if (arbre.isLeaf()):
        code[arbre.char] = prefixe
    else:
        if arbre.left != None:
            parcours(arbre.left,prefixe+'0',code)
        if arbre.right != None:
            parcours(arbre.right,prefixe+'1',code)


def dict_to_binary(dico):
    # Tree to dict
    tree_string = ""


    # Dict to binary string
    for item in dico.items():
        char = item[0]
        freq = item[1]

        char_16b = char_to_code_16_bits(char)
        freq_16b = "0" + bin(freq)[2:]

        padding = "0" if freq_16b[0]=="1" else "1"

        freq_16b = string_bin_to_16_bits(freq_16b,padding)

        tree_string+=char_16b+freq_16b
    
    # Length
    length = len(tree_string)
    bin_length = string_bin_to_16_bits("0"+str(bin(length))[2:])

    return bin_length+tree_string

def decode_tree(string):
    # first 16 bits = length
    length = int(string[:16],2)

    tree_values = string[16:16+length]

    dico = {}

    for i in range(0,len(tree_values),32):
        letter = tree_values[i:i+16]
        code = tree_values[i+16:i+32]
        letter = code_to_char_16_bits(letter)

        padding = code[0]
        code = code.lstrip('1') if padding == "1" else code.lstrip('0')
        dico[letter] = int(code,2)

    return dico, string[length+16:]



def compress(s):
    c = count(s)

    q = queue(c)

    d = duffman(q)

    # Binary dict
    d_b = dict_to_binary(c)

    r = record(d)

    e = encode(r, s)

    return d_b+e

def decompress(s):
    c,s = decode_tree(s)
    
    q = queue(c)

    d = duffman(q)

    return decode(d,s)



if __name__ == '__main__':

    s = "Goulven c'est un gros connard"

    s = open('leHorla.txt','r', encoding="utf-8").read()

    compressed = compress(s)
    decompressed = decompress(compressed)
    print(decompressed)