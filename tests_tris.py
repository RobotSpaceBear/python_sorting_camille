import copy
import random
import time

###### CONSTS #####
MAX_RANDOM = 500
MAX_ELEMENTS = 2000
MAX_ITERATIONS = 5


def tri_camille(liste):
    for i in range(0, len(liste)-1):
        smallest = min(liste[i:len(liste)])
        liste[liste[i:len(liste)].index(smallest) + i] = liste[i]

    return liste


def tri_andrei_bulle(list):
    i = 0
    while i < len(list):
        if i < len(list)-1 and list[i] > list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
            if i > 0:
                i -= 1
        else:
            i += 1


def tri_andrei_2(liste):
    quicksort(liste, 0, len(liste)-1)


def partition(liste, start, end):
    follower = leader = start
    while leader < end:
        if liste[leader] <= liste[end]:
            liste[follower], liste[leader] = liste[leader], liste[follower]
            follower += 1
        leader += 1
    liste[follower], liste[end] = liste[end], liste[follower]
    return follower


def quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end)
    quicksort(xs, start, p-1)
    quicksort(xs, p+1, end)


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
