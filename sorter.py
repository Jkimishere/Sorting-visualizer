import random

def quicksort_partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    temp = 0
    for j in range(start, end):
        if arr[j] <= pivot:
            i +=1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    i +=1
    temp = arr[i]
    arr[i] = arr[end]
    arr[end] = temp
    return i
            


def quicksort(arr, start, end, plot_func=None):
    if start < end: 
        pivot = quicksort_partition(arr, start, end)
        quicksort(arr, start, pivot - 1)
        quicksort(arr, pivot + 1, end)
    return arr




def test_quicksort(length_arr):
    test_arr = list(range(1,1000))
    random.shuffle(test_arr)

    plsman = quicksort(test_arr, 0, len(test_arr)-1)
    print(plsman == sorted(plsman))

    