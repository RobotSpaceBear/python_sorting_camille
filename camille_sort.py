# -*- coding: utf-8 -*-
import random

spam = []
for i in range(20): # génère une liste de 20 entiers aléatoires dont les valeurs sont comprises entre 1 et 100.
    spam = spam + [random.randint(1, 5)]
    
print('Liste de 20 nombres aléatoires entre 1 et 100 : ', end = '')
print(spam)

for i in range(1, 20):
    x = spam[i-1:20].index(min(spam[i-1:20])) # indice de la valeur qui est minimale parmi les valeurs non encore traitées
    spam = spam[0:i-1] + [min(spam[i-1:20])] + spam[i-1:20] # modifie la liste existante en une concaténation du début de liste qui a déjà été trié, de la valeur qui est minimale parmi les valeurs non encore traitées à ce tour, et de la partie de la liste qui n'a pas encore été traitée.
    del spam[i+x] # efface la dernière valeur minimale qui vient d'être ajoutée à la liste d'éléments déjà triés

print('Liste de 20 nombres aléatoires entre 1 et 100, triés par ordre croissant : ', end = '')
print(spam)

# bug lorsque plusieurs fois le même nombre dans la liste aléatoire...