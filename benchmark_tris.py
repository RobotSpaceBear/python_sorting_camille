import copy
import random
import time

from andrei_sort import tri_andrei_bulle
from andrei_sort import tri_andrei_2
from camille_sort import tri_camille

###### CONSTS #####
MAX_RANDOM = 500
MAX_ELEMENTS = 2000
MAX_ITERATIONS = 5

######### START #########
tempsCamille, tempsAndreiBulle, tempsAndrei2 = 0.0, 0.0, 0.0

for i in range(1, MAX_ITERATIONS):
    # generation des tableaux + copie identiques des tableau
    # pour que tout le monde travaille avec exactement les mêmes données
    liste1 = [random.randint(0, MAX_RANDOM) for i in range(MAX_ELEMENTS)]
    liste2 = copy.deepcopy(liste1)
    liste3 = copy.deepcopy(liste1)

    # tri 1
    startTime = time.time()
    tri_andrei_bulle(liste1)
    endTime = time.time()
    tempsAndreiBulle += (endTime-startTime)
    # tri 2
    startTime = time.time()
    tri_andrei_2(liste2)
    endTime = time.time()
    tempsAndrei2 += (endTime-startTime)
    # tri 3
    startTime = time.time()
    tri_camille(liste3)
    endTime = time.time()
    tempsCamille += (endTime-startTime)

print('\n\nResults for MAX_ELEMENTS=' + str(MAX_ELEMENTS)
      + '\tMAX_ITERATIONS=' + str(MAX_ITERATIONS)
      + '\tMAX_RANDOM=' + str(MAX_RANDOM))
print(str(round(tempsCamille, 5)) + 'sec -> Camille')
print(str(round(tempsAndreiBulle, 5)) + 'sec -> Andrei (tri à bulle): ')
print(str(round(tempsAndrei2, 5)) + 'sec -> Andrei (pivot sort): ')
