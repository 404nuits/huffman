#####################################################
######  Introduction à la cryptographie  	      ###
#####   Codes de Huffman             		      ###
#####################################################

from heapq import *

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
#print(F)

###  la classe Arbre

class Arbre:
    def __init__(self, lettre, gauche=None, droit=None):

        self.gauche=gauche
        self.droit=droit
        self.lettre=lettre

    def estFeuille(self):

        return self.gauche == None and self.droit == None

    def estVide(self):

        return self == None

    def __str__(self):
        return '<'+ str(self.lettre)+'.'+str(self.gauche)+'.'+str(self.droit)+'>'


###  Ex.1  construction de l'arbre d'Huffman utilisant la structure de "tas binaire"
def arbre_huffman(frequences) :
    
    # 1
    tas = [(item[1],) + (item[0],) + (Arbre(item[0]),) for item in frequences.items()]
    heapify(tas)

    # 4
    while len(tas) > 1:

        # 2
        l1 = heappop(tas)
        l2 = heappop(tas)

        # 3
        proba = l1[0] + l2[0]
        lettre = l1[1] + l2[1]
        arbre = Arbre(lettre, l1[2], l2[2])

        n = (proba, lettre, arbre)

        heappush(tas, n)
        
    #5
    return tas[0][2]


###  Ex.2  construction du code d'Huffamn

def parcours(arbre,prefixe,code) :

    if (arbre.estFeuille()):
        code[arbre.lettre] = prefixe
    else:
        if arbre.gauche != None:
            parcours(arbre.gauche,prefixe+'0',code)
        if arbre.droit != None:
            parcours(arbre.droit,prefixe+'1',code)


def code_huffman(arbre) :
    # on remplit le dictionnaire du code d'Huffman en parcourant l'arbre
    code = {}
    parcours(arbre,'',code)
    return code

###  Ex.3  encodage d'un texte contenu dans un fichier

def toBinary(dico,fichier) :
    encoded = ''
    with open(fichier,'r') as file:
        texte = file.read()
        for char in texte:
            if char in dico:
                encoded += dico[char]
            else:
                encoded += dico[' ']
    return encoded

def encodage(dico, fichier):
    bin_string = toBinary(dico, fichier)
    print(len(bin_string))
    i = 0
    buffer = bytearray()
    while i < len(bin_string):
        buffer.append(int(bin_string[i:i+8], 2))
        i += 8


    #fichier_array = fichier.split('.')
    #fichier_encoded = ''.join([fichier_array[:-1],'Encoded.',fichier_array[-1]])

    fichier_encoded = "leHorlaEncoded.txt"

    with open(fichier_encoded, 'bw') as f:
        f.write(buffer)


dico = code_huffman(arbre_huffman(F))


encodage(dico,'leHorla.txt')

###  Ex.4  décodage d'un fichier compresse

def toBinString(fichierCompresse) :

    binary_array = []

    with open(fichierCompresse,'rb') as f:
        bites = f.read()
    for b in bites:
        binary_array += bin(b)[2:]
    
    print(''.join(binary_array))


def decodage(arbre, fichierCompresse):
    bin_string = toBinString(fichierCompresse)
    decoded = ''
    root = arbre
    for bit in bin_string:
        while not arbre.estFeuille():
            pass
    #TODO : parcourir l'arbre

H = None

# decode = decodage(H,'leHorlaEncoded.txt')
# print(decode)
