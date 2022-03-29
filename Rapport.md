# RAPPORT TP Python 2 - Codes de Huffman

## Consignes
- Huffman avec fréquence (huffman.py)
- CM -> Huffman sans fréquence (lit une source et on produit un arbre)

## A rendre
Un zip avec :
- Un dossier src qui contient les fichiers sources pour les 2 (ou 3) représentations d'huffman 
- Un rapport.pdf (avec noms / prénoms)

## Organisation

Travail en binôme en pair programming. Les 2 implémentatations ont des similitudes. Travailler ensemble permet de bien comprendre les enjeux de chaque implémentation et de ne pas avoir de différence majeure dans la mise en place de celle-ci(sur les similitudes avérées).
Utilisation de GIT pour le partage des codes.

## L'utilité du fichier huffman_utils.py

Comme des classes ou fonctions sont utilisées dans les 2 implémentations des codes d'Huffman, nous avons créé un fichier huffman_utils.py.
Il sert à éviter les réécritures de code et à réutiliser au maximum les fonctions communes aux 2 implémentations d'Huffman, ainsi que des fonctions génériques comme la conversion d'un caractère sur 16 bits.

### Implémentation de la classe Arbre

L'implémentation de la classe Arbre dans le fichier huffman_utils.py est légèrement différente de celle proposée dans le TP, elle contient, en plus :
- La propriété __fréquence__
- Des fonctions de comparaison (\_\_gt\_\_ et \_\_lt\_\_)
    - Ces fonctions comparent les arbres en se basant sur leur fréquence

Ces ajouts sont utiles notamment pour indiquer à heapq sur quoi effectuer la comparaison pour trier le tas. Nous avons choisi cette implémentation car nous trouvions cela moins redondant que de créer un triplet pour chaque élément du tas, simplement pour indiquer à heapq comment les comparer.

### Méthode de prise en charge du binaire
Pour travailler avec des bits, afin de simplifier le code et la compréhension, nous travaillions avec une chaîne de caractères, composée de 0 et de 1, qui représentait notre code binaire, et ce n'est qu'au  moment de l'écriture ou de la lecture depuis fichier binaire que nous convertissions cette chaine en liste d'octets (bytearray), afin d'écriture/lire en binaire.

## Huffman sans fréquence

## Huffman avec fréquence

### NYT
Pour l'implémentation avec fréquence d'Huffman, nous avons choisi de prendre en compte les caractères n'étant pas dans le tableau de fréquences, donc de prendre en compte le NYT (Not Yet Transfered).
Pour cela, nous avons dans un premier temps, ajouté une branche NYT à l'arbre, puis nous avons assigné tous les caractères non reconnus à cette branche, accompagnés de leur charcode en binaire, codé sur 16 bits.

Nous avons fait le choix de coder le caractère sur 16 bits pour prendre en compte tout l'UTF-8, qui est sur 16 bits, car des caractères du texte proposé en entrée, "leHorla.txt", n'étaient pas présent dans l'ASCII, comme le caractère **`’`**, qui est encodé sur plus de 8 bits, rayant cette possibilité des choix qui nous avons à notre disposition.

### Exercice 1
heapq a plusieurs méthodes pour comparer les éléments de la liste, il peut :
- Si les éléments sont des triplets, comparer les premiers éléments entre eux
- Sinon, il utilise les fonctions de comparaisons basiques, comme \_\_gt\_\_ ou \_\_lt\_\_ , pour comparer ses éléments
Comme dit auparavant, nous avons donc préféré l'approche utilisant les fonctions de comparaison, car elle induisait un code moins redondant, plus compréhensible, et plus cohérent globalement.

Il est important de noter qu'avant de générer notre arbre, nous ajoutons artificellement une entrée dans le dictionnaire des fréquences, cette entrée étant le NYT, avec une fréquence de 0, afin qu'il apparaisse au plus bas dans le tableau, et pour ne pas fausser les autres valeurs des fréquences (dont la somme doit faire 1).

Dans un premier temps, on génère une liste de feuilles, chaque élément de la liste étant une instance de la classe Arbre, avec lettre et fréquence indiquées, puis on transforme cette liste en tas avec heapq, ce qui nous permet d'en avoir une version triée sur la fréquence.

Dans un second temps, on génère un arbre d'Huffman à partir de ce tas, en retirant de ce tas les 2 plus petits éléments, puis en créant une nouvelle instance d'Arbre (un nouveau Noeud), dont la lettre et la fréquence sont la concaténation des 2 retirées auparavant.

Cette nouvelle instance d'Arbre ne sera pas une feuille, puisqu'elle aura comme enfants les 2 retirés précedemment, respectivement gauche et droit.

On ajoute ensuite ce nouveau noeud au tas, et on recommence l'itération jusqu'à ce que le tas ne fasse plus qu'un élément de longueur, l'élément résultant étant l'arbre complet d'Huffman.

### Exercice 2

## Méthode de test unitaire