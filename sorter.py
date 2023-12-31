import random
import time
import matplotlib.pyplot as plt

def quicksort_partition(arr, start, end, plot_func, fignum):
    pivot = arr[end]
    i = start - 1
    temp = 0
    for j in range(start, end):
        if not plt.fignum_exists(fignum):
            return
        #time.sleep(0.03)
        if arr[j] <= pivot:
            i +=1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            plot_func(arr, 'quicksorting....')
    #time.sleep(0.03)
    i +=1
    temp = arr[i]
    arr[i] = arr[end]
    arr[end] = temp
    plot_func(arr, 'quicksorting....')
    return i
            


def quicksort(arr, start, end, plot_func, fignum):
    if not plt.fignum_exists(fignum):
        return
    if start < end: 
        pivot = quicksort_partition(arr, start, end, plot_func, fignum)
        #time.sleep(0.03)
        try:
            quicksort(arr, start, pivot - 1, plot_func, fignum)
            quicksort(arr, pivot + 1, end, plot_func, fignum)
        except TypeError:
            print("\033[1;31;40m You closed the plot. \033[m")

    return arr




def test_quicksort(length_arr):
    test_arr = list(range(1,1000))
    random.shuffle(test_arr)

    plsman = quicksort(test_arr, 0, len(test_arr)-1)
    print(plsman == sorted(plsman))

    