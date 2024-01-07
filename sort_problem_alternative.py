def find_min_max(arr, a):
    for i in range(a+1):
        min_value = float('inf')
        max_value = float('-inf')
        for j in arr:
            if j < min_value:
                min_value = j
            if j > max_value:
                max_value = j
        arr.remove(min_value)
        arr.remove(max_value)
    print(min_value, max_value)

