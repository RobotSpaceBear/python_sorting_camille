import copy
import random
import time

###### CONSTS #####
MAX_RANDOM = 1000
MAX_ELEMENTS = 1000
MAX_ITERATIONS = 5

def tri_camille(liste):
    for i in range(0, len(liste)-1):
        smallest = min(liste[i:len(liste)])
        liste[liste[i:len(liste)].index(smallest) + i]= liste[i]
    
    return liste

def tri_andrei_bulle(list):
    i = 0
    while i < len(list):        
        if i < len(list)-1 and list[i] > list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp            
            if i > 0:
                i-=1        
        else :
            i += 1

def tri_andrei_2(liste):
    return 0


######### START #########
tempsCamille, tempsAndreiBulle, tempsAndrei2 = 0.0, 0.0, 0.0

for i in range(1, MAX_ITERATIONS):
    liste1 = [random.randint(0,MAX_RANDOM) for i in range(MAX_ELEMENTS)]
    liste2 = copy.deepcopy(liste1)
    liste3 = copy.deepcopy(liste1)

    startTime = time.time()
    tri_andrei_bulle(liste1)
    endTime=time.time()
    tempsAndreiBulle += (endTime-startTime)

    startTime = time.time()
    tri_andrei_2(liste2)
    endTime=time.time()
    tempsAndrei2 += (endTime-startTime)

    startTime = time.time()
    tri_camille(liste3)
    endTime=time.time()
    tempsCamille += (endTime-startTime)

print(str(tempsCamille) + ' -> Camille')
print(str(tempsAndreiBulle) + '-> Andrei (tri à bulle): ')