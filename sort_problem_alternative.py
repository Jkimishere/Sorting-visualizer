def find_min_max(arr):
    min_value = float('inf')
    max_value = float('-inf')
    for j in arr:
        if j < min_value:
            min_value = j
        if j > max_value:
            max_value = j
    return min_value, max_value

def find_min_max_parallel(arr):
    
    set_0 = arr[:len(arr)//2]
    set_1 = arr[len(arr)//2:]
    min_value_0 = float('inf')
    max_value_0 = float('-inf')
    min_value_1 = float('inf')
    max_value_1 = float('-inf')
    print(len(set_0), len(set_1))
    for i in range(len(set_0)):
        j, k = set_0[i], set_1[i]
        if j < min_value_0:
            min_value_0 = j
        if j > max_value_0:
            max_value_0 = j
        if k < min_value_1:
            min_value_1 = k
        if k > max_value_1:
            max_value_1 = k
    #for cases where list length is odd
    if len(arr) % 2 != 0:
        mid_element = arr[len(arr)//2]
        if mid_element < min_value_0:
            min_value_0 = mid_element
        if mid_element > max_value_0:
            max_value_0 = mid_element
            
    if min_value_0 < min_value_1:
        print(f'min value is {min_value_0}')
    if min_value_0 > min_value_1:
        print(f'min value is {min_value_1}')
    if max_value_0 > max_value_1:
        print(f'max value is {max_value_0}')
    if max_value_0 < max_value_1:
        print(f'max value is {max_value_1}')


