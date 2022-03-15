################################################
## Implémentation de l'algorithme de Huffman  ##
####             Sans fréquence             ####
################################################

from collections import Counter
from heapq import heapify, heappop, heappush

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
    counter = Counter(string)
    return dict(counter)


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


    return queue


# Record
def record(queue):
    root = queue[0]
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


def compress(s):
    c = count(s)

    q = queue(c)

    d = duffman(q)

    r = record(d)

    e = encode(r, s)

    return e


def size_compare(string):
    
    compressed = compress(string)

    b_string = to_binary(string)

    print(f"Normal size : {len(b_string)}")
    print(f"Compressed size : {len(compressed)}")

    return "prout"

if __name__ == '__main__':

    s = "Goulven c'est un connard"

    size_compare(s)