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
            
    return list


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
