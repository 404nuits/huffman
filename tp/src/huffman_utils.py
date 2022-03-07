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

    def isLeaf(self):
        return self.left == None and self.right == None
    def isEmpty(self):
        return self == None
    def __lt__(self, other):
        return self.frequency < other.frequency
    def __gt__(self, other):
        return self.frequency > other.frequency
    def __str__(self):
        return '<'+ str(self.char)+'.'+str(self.left)+'.'+str(self.right)+'>'
