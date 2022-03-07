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



if __name__ == '__main__':

    s = "Bonjour je m'appelle ewen"

    c = count(s)

    q = queue(c)

    d = duffman(q)

    print(list(d)[0])